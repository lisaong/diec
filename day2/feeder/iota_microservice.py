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

import sys
sys.path.append('..')
import iota_client

class IotaMicroservice(MqttMicroservice):
    def __init__(self):
        channels = [
            'iota'
        ]

        self.wallets = json.load(open('iota_wallets.json', 'r'))
        MqttMicroservice.__init__(self, channels)

    def on_message(self, topic, payload):
        """Specialised message handler for this service"""
        print(topic, payload)

        cost = self.compute_cost(payload)
        print(cost)

        # conduct iota transaction
        bundle_hash = self.do_transaction(payload['id'], cost)
        if bundle_hash:
            self.publish_message('dispenser', str(bundle_hash))

    def compute_cost(self, payload):
        nutrients = {v for k, v in payload.items() if k not in ('id')}

        # naive way - add all the numbers up
        return reduce(lambda x, y: x + y, nutrients)

    def do_transaction(self, id, cost):
        bundle_hash = None
        try:
            for sender in self.wallets['birds']:
                if sender['id'] == id:
                    bundle_hash = iota_client.do_transaction(sender['seed'],
                        self.wallets['dispenser'], cost, message=id)
                    break

        except Exception as e:
            # Seed may be invalid
            print('Exception:', e)

        return bundle_hash

    def test(self):
        payload = json.loads("pub: {'vitamin A': 15, 'vitamin D3': 20, 'omega-3': 20, 'omega-6': 23, 'lysine': 18, 'id': '123'}")
        while(True):
            self.on_message('iota', payload)
    
if __name__ == '__main__':
    service = IotaMicroservice()
    service.parse_args('IOTA Microservice')
    #service.run()
    service.test()
