#
# IOTA Microservice
#
# Provides IOTA services for the IOTA bird feeder system.
# Monitors MQTT triggers for transaction requests, performs
# the trasactions, and posts the results when completed.
#
# Author: Lisa Ong, NUS/ISS
#

from functools import reduce
import json
import config # common configuration
from base_microservices import *

class IotaMicroservice(MqttMicroservice):
    def __init__(self):
        channels = [
            'iota'
        ]

        self.wallets = json.load(open('iota_wallets.json', 'r'))
        MqttMicroservice.__init__(self, channels)
        
        # unit test
        # self.on_message('test', {'vitamin A': 50, 'vitamin D3': 10, 'omega-3': 30, 'omega-6': 13, 'lysine': 15, 'id': '456'})

    def on_message(self, topic, payload):
        """Specialised message handler for this service"""
        print(topic, payload)

        price = self.compute_price(payload)
        print(price)

        # initiate iota transaction

        # self.publish_message('dispenser', 'helloXXXXXXXXX')

    def compute_price(self, payload):
        nutrients = {v for k, v in payload.items() if k not in ('id')}

        # naive way - add all the numbers up
        return reduce(lambda x, y: x + y, nutrients)

if __name__ == '__main__':
    service = IotaMicroservice()
    service.parse_args('IOTA Microservice')
    service.run()