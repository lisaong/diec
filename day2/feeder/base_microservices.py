#
# Base Microservice
#
# Base microservice classes
# Abstract the communication protocol from derived classes
#
# Author: Lisa Ong, NUS/ISS
#

import argparse
import json

# References: https://www.eclipse.org/paho/clients/python/docs/
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def _on_connect(client, userdata, flags, rc):
    userdata.on_connect()

def _on_message(client, userdata, msg):
    try:
        # JSON requires doublequotes instead of singlequotes
        # decode converts byte array to str for JSON parser
        payload = json.loads(msg.payload.replace(b"'", b'"').decode('utf-8'))
        userdata.on_message(msg.topic, payload)
    except Exception as e:
        # exceptions tend to get swallowed up in callbacks
        # print them here
        print('Exception:', e)

class MqttMicroservice:
    def __init__(self, channels):

        # protocol-specific settings
        self.client = mqtt.Client(userdata=self)
        self.client.on_connect = _on_connect
        self.client.on_message = _on_message
        self.channels = channels
        self.hostname = 'localhost'
        self.port = 1883

    def on_connect(self):
        """Called when the MQTT client is connected
        """
        for channel in self.channels:
            topic = self.topic_id + '/' + channel
            self.client.subscribe(topic)
            print('Subscribed to:' + topic)

    def on_message(self, topic, payload):
        """Called when an MQTT client is received
        """
        print(topic, payload)

    def publish_message(self, channel, msg):
        """Publishes a message to an MQTT topic
        """
        print('pub:', msg)
        publish.single(self.topic_id + '/' + channel,
            payload=json.dumps(msg), retain=False,
            hostname=self.hostname, port=self.port,
            protocol=mqtt.MQTTv311)

    def connect(self, start=False):
        self.client.connect(self.hostname, self.port)
        if start:
            # https://www.eclipse.org/paho/clients/python/docs/#network-loop
            self.client.loop_start()

    def disconnect(self):
        self.client.disconnect()

    def run(self):
        """Called to run the service
        """
        try:
            self.connect()
            self.client.loop_forever()
        finally:
            self.disconnect() # cleanly disconnect

    def parse_args(self, description):
        parser = argparse.ArgumentParser(description=description)

        parser.add_argument('topic_id', type=str,
            help='Top level topic identifier, e.g. /dev/ttyACM0 or COM4')
        parser.add_argument('--hostname', type=str, default='localhost',
            help='MQTT broker hostname, defaults to TCP localhost')
        parser.add_argument('--port', type=int, default=1883, help='MQTT broker port, defaults to 1883')

        args = parser.parse_args()
        self.topic_id = args.topic_id

        if args.hostname is not None:
            self.hostname = args.hostname
        if args.port is not None:
            self.port = args.port


if __name__ == '__main__':
    # for testing purposes only
    service = MqttMicroservice(['stream'])
    service.parse_args('MQTT Microservice')
    service.run()
