import paho.mqtt.publish as publish
import argparse

def connect():
    pass

def disconnect():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sends a Kapua connection / disconnection request')
    parser.add_argument('command', type=str, choices=['connect', 'disconnect'])

    args = parser.parse_args()

    if args.command == 'connect':
        connect()
    elif args.command == 'disconnect':
        disconnect()



