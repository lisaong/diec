#
# Nutrient Microservice
#
# The business logic of the IOTA bird feeder system.
# Monitors Micro:bit MQTT events, determines the amount
# of nutrient to dispense, and performs IOTA transactions
#
# Author: Lisa Ong, NUS/ISS
#

import config # common configuration
from base_microservices import *

class NutrientMicroservice(MqttMicroservice):
    def __init__(self, args):
        channels = [
            'arrival',
            'stream'
        ]
        MqttMicroservice.__init__(self, args, channels)

    def on_message(self, msg):
        """Specialised message handler for this service"""
        print(msg.topic, str(msg.payload))

if __name__ == '__main__':
    args = config.parse_args('IOTA bird feeder system')
    service = NutrientMicroservice(args)
    service.run()
