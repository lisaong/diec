#
# Micro:bit IO Test
# Receives data (e.g. button presses, accelerometer readings) via the serial interface
#
# Author: Lisa Ong, NUS/ISS
#

import argparse
import serial

parser = argparse.ArgumentParser(description='Tests serial connection to micro:bit')
parser.add_argument('port', type=str, help='serial port identified e.g. /dev/ttyACM0')
args = parser.parse_args()

s = serial.Serial(args.port)
s.baudrate = 115200

while True:
    data = s.readline()
    print(data)
