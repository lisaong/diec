#
# Base Microservice
#
# Base microservice classes
# Abstract the communication protocol from derived classes
#
# Author: Lisa Ong, NUS/ISS
#

import argparse

# References: https://www.eclipse.org/paho/clients/python/docs/
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def _on_connect(client, userdata, flags, rc):
    userdata.on_connect()

def _on_message(client, userdata, msg):
    try:
        userdata.on_message(msg)
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

    def on_message(self, msg):
        """Called when an MQTT client is received
        """
        print(msg.topic, msg.payload)

    def publish_message(self, channel, msg):
        """Publishes a message to an MQTT topic
        """
        publish.single(self.topic_id + '/' + channel,
            payload=msg, retain=False,
            hostname=self.hostname, port=self.port,
            protocol=mqtt.MQTTv311)

    def run(self):
        """Called to run the service
        """
        try:
            self.client.connect(self.hostname, self.port)
            self.client.loop_forever()
        finally:
            self.client.disconnect() # cleanly disconnect

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
