#
# Common Configuration
#
# Author: Lisa Ong, NUS/ISS
#
import argparse

window_size = 100
data_columns = ['ts', 'gest', 'accX', 'accY', 'accZ', 'temp', 'head']

def parse_args(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('topic_id', type=str,
        help='Top level topic identifier, e.g. dev/ttyACM0 or COM4')
    parser.add_argument('--hostname', type=str, default='localhost',
        help='MQTT broker hostname, defaults to TCP localhost')
    parser.add_argument('--port', type=int, default=1883, help='MQTT broker port, defaults to 1883')

    args = parser.parse_args()
    if args.hostname is None:
       args.hostname = 'localhost'
    if args.port is None:
        args.port = 1883
    return args
