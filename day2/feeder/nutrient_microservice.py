#
# Nutrient Microservice
#
# The business logic of the IOTA bird feeder system.
# Monitors Micro:bit MQTT events, determines the amount
# of nutrient to dispense, and performs IOTA transactions
#
# Author: Lisa Ong, NUS/ISS
#

from collections import deque
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
        if 'arrival' in topic:
            self.on_arrival(payload)
        else:
            self.on_stream(payload)

    def on_arrival(self, payload):
        # bird has arrived

        # run task graph that computes how much feed is needed
        print(payload)
        result = get(self.dsk, 'combine')
        print(result)

        # create iota transaction
        self.publish_message('iota', result)

    def on_stream(self, payload):
        # automatically discards items at the opposite end if full
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
            'combine': (NutrientMicroservice.combine, ['analyze-%d' % i for i in range(1, 2)])
        }

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
        print('analyze')
        window_size = 10
        num_windows = len(data) // window_size

        results = []
        for i in range(num_windows-1):
            window = data[i*window_size:(i+1)*window_size]

            # list of dictionaries => dictionary of lists
            ld = {k: [dic[k] for dic in window] for k in window[0]}

            results.append({
                'gest_common': mode(ld['gest'])
            })

            # compute mean and std
            for k in ['accX_mg', 'accY_mg', 'accZ_mg', 'temp_C', 'head_degN']:
                results[-1][k + '_mean'] = mean(ld[k])
                results[-1][k + '_std'] = stdev(ld[k])

        return results

    def combine(data):
        """Combines all the different lists into 1 list"""
        print('combine')
        return reduce(lambda x, y: x + y, data)

if __name__ == '__main__':
    service = NutrientMicroservice()
    service.parse_args('Nutrient Microservice')
    service.run()
