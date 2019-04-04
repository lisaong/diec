#
# Base Microservice
#
# Base microservice classes
# Abstract the communication protocol from derived classes
#
# Author: Lisa Ong, NUS/ISS
#

# References: https://www.eclipse.org/paho/clients/python/docs/
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def on_connect(client, userdata, flags, rc):
    userdata._on_connect()

def on_message(client, userdata, msg):
    userdata.on_message(msg)

class MqttMicroservice:
    def __init__(self, args, channels):

        # protocol-specific settings
        self.client = mqtt.Client(userdata=self)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.hostname = args.hostname
        self.port = args.port
        self.topic_id = args.topic_id
        self.channels = channels

    def _on_connect(self):
        """Called when the MQTT client is connected

        Should not be overwritten by subclasses.
        """
        for channel in self.channels:
            topic = self.topic_id + '/' + channel
            self.client.subscribe(topic)
            print('Subscribed to:' + topic)

    def on_message(self, msg):
        """Called when an MQTT client is received

        Should be overridden by subclasses
        """
        print(msg.topic, msg.payload)

    def publish_message(self, channel, msg):
        """Publishes a message to an MQTT topic

        Should not be overwritten by subclasses.
        """
        publish.single(self.topic_id + '/' + channel,
            payload=msg, retain=False,
            hostname=self.hostname, port=self.port,
            protocol=mqtt.MQTTv311)

    def run(self):
        """Called to run the service

        Should not be overridden by subclasses
        """
        try:
            self.client.connect(self.hostname, self.port)
            self.client.loop_forever()
        finally:
            self.client.disconnect() # cleanly disconnect