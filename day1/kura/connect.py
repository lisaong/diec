import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import argparse
import json

import kurapayload_pb2
from google.protobuf import json_format

client_id='02:42:AC:11:00:02'

# default username and password created on Kapua,
# associated with this device
username='user1'
password='Kapu@12345678'

def send_message(hostname, port, subtopic, json_payload):
    topic='$EDC/diec1/' + client_id + '/MQTT/' + subtopic

    pb = json_format.Parse(json.dumps(json_payload),
                           kurapayload_pb2.KuraPayload(),
                           ignore_unknown_fields=False)

    publish.single(topic, payload=pb.SerializeToString(), qos=0, retain=False,
        hostname=hostname, port=port, keepalive=60, will=None,
        auth={'username':username, 'password':password}, tls=None,
        protocol=mqtt.MQTTv311, transport='tcp')

def send_event(hostname, port, event):
    topic='$EDC/diec1/' + client_id + '/MQTT/' + event

    # Event,CONNECT,,DeviceId,02:42:AC:11:00:02,,Username,user1
    payload = 'Event,' + event + ',DeviceId,' + client_id + \
              ',,Username,' + username
    print(payload)

    publish.single(topic, payload=payload, qos=0, retain=False,
        hostname=hostname, port=port, keepalive=60, will=None,
        auth={'username':username, 'password':password}, tls=None,
        protocol=mqtt.MQTTv311, transport='tcp')

def disconnect(hostname, port):
    with open('disconnect_template.json') as f:
        payload = json.load(f)
    print(payload)

    send_event(hostname, port, 'DISCONNECT')
    send_message(hostname, port, 'DC', payload)

def connect(hostname, port):
    with open('connect_template.json') as f:
        payload = json.load(f)
    print(payload)

    send_message(hostname, port, 'BIRTH', payload)
    send_event(hostname, port, 'CONNECT')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sends a Kapua connection / disconnection request')
    parser.add_argument('command', type=str, choices=['connect', 'disconnect'])
    parser.add_argument('hostname', type=str, help='Kapua MQTT url hostname, e.g. 0.tcp.ngrok.io')
    parser.add_argument('port', type=int, help='Kapua MQTT url port, e.g. 11418')

    args = parser.parse_args()

    hostname = args.hostname
    port = args.port

    if args.command == 'connect':
        connect(hostname, port)
    elif args.command == 'disconnect':
        disconnect(hostname, port)



