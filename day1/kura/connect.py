import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import getmac
import argparse

# TODO: update this to the Kapua MQTT server hostname & port
hostname='0.tcp.ngrok.io'
port=11418

# default username and password created on Kapua,
# associated with this device
username='user1'
password='Kapu@12345678'

# assume we are running the docker version of kapu
mac=getmac.get_mac_address(interface='docker0')

def connect():
    # send a message to connect
    topic=f'$EDC/diec1/{mac}/MQTT/BIRTH'

    publish.single(topic, payload='test', qos=0, retain=False,
        hostname=hostname, port=port, keepalive=60, will=None,
        auth={'username':username, 'password':password}, tls=None,
        protocol=mqtt.MQTTv311, transport='tcp')

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



