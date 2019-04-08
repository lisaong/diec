#
# Common Configuration
#
# Author: Lisa Ong, NUS/ISS
#
import os

# Data format from Micro:bit
DATA_COLUMNS = ['ts_ms', 'gest', 'accX_mg', 'accY_mg',
    'accZ_mg', 'temp_C', 'head_degN']

DATA_TYPES = [int, str, int, int, int, int, int]

WINDOW_SIZE = os.getenv('FEEDER_DATA_WINDOW_SIZE', 1000)

# https://microbit-micropython.readthedocs.io/en/latest/tutorials/gestures.html
GESTURES = {'up', 'down', 'left', 'right',
    'face up', 'face down', 'freefall',
    '3g', '6g', '8g', 'shake'}
