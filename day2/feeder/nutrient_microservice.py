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

import config
from base_microservices import *

class NutrientMicroservice(MqttMicroservice):
    def __init__(self):
        channels = [
            'arrival',
            'stream'
        ]

        self.data = None
        self.window_size = config.WINDOW_SIZE

        MqttMicroservice.__init__(self, channels)

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
        # run task graph
        # create iota transaction
        try:
            self.data.to_csv('test-*.csv', index=False)
            # self.publish_message('iota', msg.payload)
            print(payload)

        except Exception as e:
            # exceptions tend to get swallowed up in callbacks
            # print them here
            print('Exception:', e)

    def on_stream(self, payload):
        try:
            # collect data in a buffer
            # this data will be processed on arrival
            pass
        except Exception as e:
            print('Exception:', e)

    def run(self):
        # initialisation before running the service
        # setup local cluster
        # create simple task graph to process the data in parallel

        MqttMicroservice.run()

if __name__ == '__main__':
    service = NutrientMicroservice()
    service.parse_args('Nutrient Microservice')
    service.run()
