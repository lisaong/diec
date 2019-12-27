#
# Nutrient Microservice
#
# The business logic of the IOTA bird feeder system.
# Monitors Micro:bit MQTT events, determines the amount
# of nutrient to dispense, and performs IOTA transactions
#
# Author: Lisa Ong, NUS/ISS
#

from collections import deque, Counter
from dask.multiprocessing import get
from itertools import islice
from functools import reduce

# numpy is too heavyweight, use statistics library
from statistics import mean, mode, stdev

import config
from base_microservices import *

class NutrientMicroservice(MqttMicroservice):
    def __init__(self):
        channels = [
            'arrival',
            'stream'
        ]

        # queue to hold samples
        self.data_queue = deque(maxlen=config.BUFFER_SIZE)

        MqttMicroservice.__init__(self, channels)

    def on_message(self, topic, payload):
        """Specialised message handler for this service"""
        print(topic, payload)
        if 'arrival' in topic:
            self.on_arrival(payload)
        else:
            self.on_stream(payload)

    def on_arrival(self, payload):
        # bird has arrived

        # run task graph that processes sensor data
        data = get(self.dsk, 'combine')

        # determine nutrient profile based on bird and sensor data
        if data:
            profile = self.get_nutrient_profile(payload['id'], data)

            # create iota transaction
            if profile:
                self.publish_message('iota', profile)

    def on_stream(self, payload):
        # a fixed size deque automatically discards items at the opposite end if full
        self.data_queue.append(payload)

        # To see the loop-around, you can set FEEDER_DATA_BUFFER_SIZE
        # to a small number (e.g. 10), and then uncomment this:
        # print('leftmost entry', self.data_queue[0])
        # print('rightmost entry', self.data_queue[-1])

    def run(self):
        """Overrides MqttMicroservice.run with service-specific initialization"""
        # Create simple task graph to process the data in parallel
        # https://docs.dask.org/en/latest/custom-graphs.html
        batch_size = config.BUFFER_SIZE // 2
        self.dsk = {
            'load-1': (NutrientMicroservice.load, self.data_queue, 0, batch_size),
            'load-2': (NutrientMicroservice.load, self.data_queue, batch_size*1, batch_size),
            'clean-1': (NutrientMicroservice.clean, 'load-1'),
            'clean-2': (NutrientMicroservice.clean, 'load-2'),
            'analyze-1': (NutrientMicroservice.analyze, 'clean-1'),
            'analyze-2': (NutrientMicroservice.analyze, 'clean-2'),
            'combine': (NutrientMicroservice.combine, ['analyze-1', 'analyze-2']),
        }

        # pip install graphviz
        # Download: https://graphviz.gitlab.io/download/
        #
        # from dask import visualize
        # visualize(self.dsk, filename='dask.pdf')

        # Run the service
        MqttMicroservice.run(self)

    def load(queue, offset, batch_size):
        """Loads batch_size entries from the queue, starting at offset"""
        print('load: offset', offset)
        return list(islice(queue, offset, offset+batch_size))

    def clean(data):
        """Cleans data by removing entries with missing/invalid gestures"""
        print('clean')
        return list(filter(lambda x: x['gest'] in config.GESTURES, data))

    def analyze(data):
        """Extracts features from the data using window size samples
        - most common gesture
        - mean and standard deviation
           - accelerometer
           - heading
           - temperature
        """
        window_size = 10
        num_windows = len(data) // window_size

        results = []
        for i in range(num_windows-1):
            window = data[i*window_size:(i+1)*window_size]

            # list of dictionaries => dictionary of lists
            ld = {k: [dic[k] for dic in window] for k in window[0]}

            results.append({
                # if no most common value, will return any of the
                # most common. Returns a list of tuples [('shake', 5)]
                'gest_common': Counter(ld['gest']).most_common(1)[0]
            })

            # compute mean and std
            for k in ['accX_mg', 'accY_mg', 'accZ_mg', 'temp_C', 'head_degN']:
                results[-1][k + '_mean'] = mean(ld[k])
                results[-1][k + '_std'] = stdev(ld[k])

        print('analyze:', len(results))
        return results

    def combine(data):
        """Combines all the different lists into 1 list"""
        results = reduce(lambda x, y: x + y, data) 
        print('combine:', len(results))
        return results

    def get_nutrient_profile(self, id, data):
        """Applies a simple heuristic to determine nutrient profile"""
        # dosages in mg (note: not actual dosages)
        base_plan = {
            'vitamin A': 15,
            'vitamin D3': 20,
            'omega-3': 20,
            'omega-6': 23,
            'lysine': 18
        }

        result = {}

        # TODO: fingerprinting using sensor data instead
        # of this naive approach
        # last_gest = data[-1]['gest_common'] # (gesture, count)
        # if (id == '123' and last_gest[0] == 'left' or
        #    id == '456' and last_gest[0] == 'right'):
        if (id == '123' or id == '456'):
            result = base_plan
            result['id'] = id
            print('nutrient profile', result)
        return result

if __name__ == '__main__':
    service = NutrientMicroservice()
    service.parse_args('Nutrient Microservice')
    service.run()
