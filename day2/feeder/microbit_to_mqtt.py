#
# Micro:bit to MQTT
# Relays micro:bit events to MQTT
#
# Author: Lisa Ong, NUS/ISS
#

import os
import sys
import time
import asyncio
import serial_asyncio

import config # common configuration
from base_microservices import *

BAUDRATE = 115200
service = None # global to give SerialIo access to the service

class SerialIo(asyncio.Protocol):
    def connection_made(self, transport):
        """Implements asyncio.Protocol.connection_made()
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        self.transport = transport
        self.buffer = b''
        print('port opened', transport)

    def data_received(self, data):
        """Implements asyncio.Protocol.data_received
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        self.buffer = self.buffer + data

        if b'\n' in data:
            service.send_message(self.buffer)
        self.buffer = b''

    def connection_lost(self, exc):
        """Implements asyncio.Protocol.connection_lost
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        print('port closed')
        self.transport.loop.stop()

class SerialToMqttMicroservice(MqttMicroservice):
    def __init__(self):
        channels = [
            'dispenser'
        ]
        MqttMicroservice.__init__(self, channels)

    def run(self):
        """Overrides MqttMicroservice.run"""
        self.start_time = int(time.time() * 1000)

        try:
            # connect to serial
            loop = asyncio.get_event_loop()
            coro = serial_asyncio.create_serial_connection(loop, SerialIo,
                self.topic_id, baudrate=BAUDRATE)

            # connect to MQTT
            self.connect()

            loop.run_until_complete(coro)
            loop.run_forever()

        finally:
            # disconnect from MQTT
            self.disconnect()
            loop.close()

    def send_message(self, buffer):
        """Sends a message to the appropriate MQTT channel"""
        # relative timestamp msec
        timestamp = int(time.time() * 1000) - self.start_time

        data = buffer.decode().strip()
        fields = data.split(',')

        if len(fields) > 0:
            if 'arrival' in fields[0] and len(fields) > 1:
                # arrival message
                message = {'ts': timestamp, 'id': fields[1]}
                self.publish_message('arrival', str(message))
            else:
                # treat as stream message
                fields = config.DATA_COLUMNS
                values = [timestamp] + data.split(',')

                if len(fields) == len(values): # no missing values
                    # convert to dictionary, performing type coercion as well
                    message = {k:d(v) for k, v, d in zip(fields, values, config.DATA_TYPES)}
                    self.publish_message('stream', str(message))

    def on_message(self, topic, payload):
        """Overrides MqttMicroservice.on_message"""
        print(topic, payload)

if __name__=="__main__":
    service = SerialToMqttMicroservice()
    service.parse_args('Serial to MQTT Microservice')
    service.run()
