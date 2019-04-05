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
        """Overrides MqttMicroservice.on_message"""
        try:
            # JSON requires doublequotes instead of singlequotes
            payload = json.loads(msg.payload.replace(b"'", b'"'))

            if 'arrival' in msg.topic:
                self.on_arrival(payload)
            else:
                self.on_stream(payload)

        except Exception as e:
            # exceptions tend to get swallowed up in callbacks
            # print them here
            print('Exception:', e)

    def on_arrival(self, payload):
        # bird has arrived
        # compute how much feed is needed
        # run task graph
        # create iota transaction

        # self.publish_message('iota', msg.payload)
        print(payload)

    def on_stream(self, payload):
        # fill up sliding-window buffer
        pass

    def run(self):
        """Overrides MqttMicroservice.run"""
        # initialisation before running the service
        # setup local cluster
        # create simple task graph to process the data in parallel

        # run the service
        MqttMicroservice.run()

if __name__ == '__main__':
    service = NutrientMicroservice()
    service.parse_args('Nutrient Microservice')
    service.run()
