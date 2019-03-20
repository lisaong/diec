import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import argparse
import json

import kurapayload_pb2
from google.protobuf import json_format

# TODO: update this to the Kapua MQTT server hostname & port
hostname='0.tcp.ngrok.io'
port=11418
client_id='02:42:AC:11:00:02'

# default username and password created on Kapua,
# associated with this device
username='user1'
password='Kapu@12345678'

def send_message(subtopic, json_payload):
    topic='$EDC/diec1/' + client_id + '/MQTT/' + subtopic

    pb = json_format.Parse(json.dumps(json_payload),
                           kurapayload_pb2.KuraPayload(),
                           ignore_unknown_fields=False)

    publish.single(topic, payload=pb.SerializeToString(), qos=0, retain=False,
        hostname=hostname, port=port, keepalive=60, will=None,
        auth={'username':username, 'password':password}, tls=None,
        protocol=mqtt.MQTTv311, transport='tcp')

def send_event(event):
    topic='$EDC/diec1/' + client_id + '/MQTT/' + event

    # Event,CONNECT,,DeviceId,02:42:AC:11:00:02,,Username,user1
    payload = 'Event,' + event + ',DeviceId,' + client_id + \
              ',,Username,' + username
    print(payload)

    publish.single(topic, payload=payload, qos=0, retain=False,
        hostname=hostname, port=port, keepalive=60, will=None,
        auth={'username':username, 'password':password}, tls=None,
        protocol=mqtt.MQTTv311, transport='tcp')

def disconnect():
    with open('disconnect_template.json') as f:
        payload = json.load(f)
    print(payload)

    send_event('DISCONNECT')
    send_message('DC', payload)

def connect(subtopic='BIRTH'):
    with open('connect_template.json') as f:
        payload = json.load(f)
    print(payload)

    send_message('BIRTH', payload)
    send_event('CONNECT')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sends a Kapua connection / disconnection request')
    parser.add_argument('command', type=str, choices=['connect', 'disconnect'])

    args = parser.parse_args()

    if args.command == 'connect':
        connect()
    elif args.command == 'disconnect':
        disconnect()



