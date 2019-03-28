#
# Micro:bit IO MQTT
# Posts events (e.g. button presses, accelerometer readings) to MQTT
#
# Author: Lisa Ong, NUS/ISS
#

import os
import sys
import time
import argparse
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

sys.path.append(os.path.join('..','ext', 'bitio', 'src'))

def send_event(args, subtopic, message=None):
    publish.single(args.topic + '/' + subtopic, payload=message,
       qos=0, hostname=args.hostname, port=args.port)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Posts events about the micro:bit to MQTT')
    parser.add_argument('topic', type=str, help='Top level topic identifier e.g. microbit1')
    parser.add_argument('--hostname', type=str, default='localhost', help='MQTT broker hostname')
    parser.add_argument('--port', type=int, default=1883, help='MQTT broker port, defaults to 1883')

    args = parser.parse_args()
    if args.hostname is None:
       args.hostname = 'localhost'
    if args.port is None:
        args.port = 1883


    # this will trigger discovery if no previous micro:bit has been found
    # to reset, delete the portscan.cache file
    import microbit

    while True:
        time.sleep(0.25)
        if microbit.button_a.was_pressed():
            print('Button A pressed')
            send_event(args, 'button', 'a')

