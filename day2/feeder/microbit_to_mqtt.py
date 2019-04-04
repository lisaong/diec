#
# Micro:bit to MQTT
# Relays micro:bit events to MQTT
#
# Author: Lisa Ong, NUS/ISS
#

import os
import sys
import time
import argparse
import json
import config
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import serial

SERIAL_BAUDRATE = 115200

def send_event(args, subtopic, message):
    # ensure that message is a string
    print(message)
    
    if args.serial_port[0] == b'/':
        # drop the initial / from the topic (dev/ttyXXXX) if
        # if it begins with /, because MQTT topics use
        # this as topic separator
        topic = args.serial_port[1:]
    else:
        topic = args.serial_port

    publish.single(topic + '/' + subtopic, payload=str(message),
       retain=False, hostname=args.hostname, port=args.port,
       protocol=mqtt.MQTTv311)

def send_arrival(args, timestamp, id):
    message = {'ts': timestamp, 'id': id}
    send_event(args, 'arrival', message)

def send_data(args, timestamp, data):
    fields = config.DATA_COLUMNS
    values = [timestamp] + data.split(',')

    if len(fields) == len(values): # no missing values
        # convert to dictionary, performing type coercion as well
        message = {k:d(v) for k, v, d in zip(fields, values, config.DATA_TYPES)}
        send_event(args, 'stream', message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Relays micro:bit events to MQTT')
    parser.add_argument('serial_port', type=str,
        help='Micro:bit serial port, e.g. /dev/ttyACM0 or COM4')
    parser.add_argument('--hostname', type=str, default='localhost',
        help='MQTT broker hostname, defaults to TCP localhost')
    parser.add_argument('--port', type=int, default=1883, help='MQTT broker port, defaults to 1883')

    args = parser.parse_args()
    if args.hostname is None:
       args.hostname = 'localhost'
    if args.port is None:
        args.port = 1883

    s = serial.Serial(args.serial_port)
    s.baudrate = SERIAL_BAUDRATE

    while True:
        data = s.readline()
        timestamp = int(time.time())

        # minimal processing for simplicity and flexibility
        data = data.decode().strip()
        fields = data.split(',')

        if len(fields) > 0:
            if 'arrival' in fields[0] and len(fields) > 1:
                # arrival message
                send_arrival(args, timestamp, fields[1])
            else:
                # treat as stream message
                send_data(args, timestamp, data)

