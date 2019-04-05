#
# IOTA Microservice
#
# Provides IOTA services for the IOTA bird feeder system.
# Monitors MQTT triggers for transaction requests, performs
# the trasactions, and posts the results when completed.
#
# Author: Lisa Ong, NUS/ISS
#

import config # common configuration
from base_microservices import *

class IotaMicroservice(MqttMicroservice):
    def __init__(self):
        channels = [
            'iota'
        ]
        MqttMicroservice.__init__(self, channels)

    def on_message(self, msg):
        """Specialised message handler for this service"""
        print(msg.topic, msg.payload)

if __name__ == '__main__':
    service = IotaMicroservice()
    service.parse_args('IOTA Microservice')
    service.run()