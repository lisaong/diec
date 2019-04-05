#
# Common Configuration
#
# Author: Lisa Ong, NUS/ISS
#

# Data format from Micro:bit
DATA_COLUMNS = ['ts_ms', 'gest', 'accX_mg', 'accY_mg', 'accZ_mg', 'temp_C', 'head_degN']
DATA_TYPES = [int, str, int, int, int, int, int]

WINDOW_SIZE = 100