import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import argparse
import json

import kurapayload_pb2
from google.protobuf import json_format

# default username and password created on Kapua,
# associated with this device
username='user1'
password='Kapu@12345678'

def send_message(args, subtopic, json_payload):
    topic='$EDC/diec1/' + args.client_id + '/MQTT/' + subtopic

    pb = json_format.Parse(json.dumps(json_payload),
                           kurapayload_pb2.KuraPayload(),
                           ignore_unknown_fields=False)

    publish.single(topic, payload=pb.SerializeToString(), qos=0, retain=False,
        hostname=args.hostname, port=args.port, keepalive=60, will=None,
        auth={'username': username, 'password': password}, tls=None,
        protocol=mqtt.MQTTv311, transport='tcp')

def death(args):
    with open('disconnect_template.json') as f:
        payload = json.load(f)
    print(payload)

    send_message(args, 'DC', payload)

def birth(args):
    with open('connect_template.json') as f:
        payload = json.load(f)
    print(payload)

    send_message(args, 'BIRTH', payload)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sends a Kapua birth / death request')
    parser.add_argument('command', type=str, choices=['birth', 'death'])
    parser.add_argument('hostname', type=str, help='Kapua MQTT url hostname, e.g. 0.tcp.ngrok.io')
    parser.add_argument('port', type=int, help='Kapua MQTT url port, e.g. 11418')
    parser.add_argument('client_id', type=str, help='The client id for a Kura device, e.g. 02:42:AC:11:00:02')

    args = parser.parse_args()

    if birth.command == 'birth':
        connect(args)
    elif args.command == 'death':
        death(args)



