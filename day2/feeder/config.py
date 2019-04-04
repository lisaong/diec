#
# Common Configuration
#
# Author: Lisa Ong, NUS/ISS
#
import argparse

# Data format from Micro:bit
DATA_COLUMNS = ['ts', 'gest', 'accX_mg', 'accY_mg', 'accZ_mg', 'temp_C', 'head_degN']
DATA_TYPES = [int, str, int, int, int, int, int]

# Some of these should eventually become environmental variables
# so that we can configure when containerised
WINDOW_SIZE = 100
DASK_PARTITIONS = 4 # typically set to number of cores

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
