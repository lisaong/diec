#
# Nutrient Microservice
#
# The business logic of the IOTA bird feeder system.
# Monitors Micro:bit MQTT events, determines the amount
# of nutrient to dispense, and performs IOTA transactions
#
# Author: Lisa Ong, NUS/ISS
#

import json
import pandas as pd
import config # common configuration
from base_microservices import *

class NutrientMicroservice(MqttMicroservice):
    def __init__(self, args, window=100):
        channels = [
            'arrival',
            'stream'
        ]

        self.data = pd.DataFrame(columns=config.data_columns)
        self.window_size = config.window_size

        MqttMicroservice.__init__(self, args, channels)

    def on_message(self, msg):
        """Specialised message handler for this service"""

        # JSON requires doublequotes instead of singlequotes
        payload = json.loads(msg.payload.replace(b"'", b'"'))

        if 'arrival' in msg.topic:
            self.on_arrival(payload)
        else:
            self.on_stream(payload)

    def on_arrival(self, payload):
        # bird has arrived
        # compute how much feed is needed
        # create iota transaction
        try:
        # self.publish_message('iota', msg.payload)
            print(payload)

        except Exception as e:
            # exceptions tend to get swallowed up in callbacks
            # print them here
            print('Exception:', e)

    def on_stream(self, payload):
        # update rolling mean
        try:
            print(payload['data'].split(','))

            #self.data.append() = pd.DataFrame(columns=['timestamp', 'gesture',
            #    'accX', 'accY', 'accZ', 'temperature', 'heading'])

        except Exception as e:
            print('Exception:', e)

if __name__ == '__main__':
    args = config.parse_args('IOTA bird feeder system')
    service = NutrientMicroservice(args)
    service.run()
