#
# Acquires data from micro:bit using serial IO
# Author: Lisa Ong, NUS/ISS
#

import serialio

# Refer to the documentation below on how to find the serial port for the micro:bit
# https://support.microbit.org/support/solutions/articles/19000022103-outputing-serial-data-from-the-micro-bit-to-a-computer

COMPORT = 'COM3' # Example Windows port
# COMPORT = '/dev/cu.usbmodem144102' # Example MacOS port

BAUDRATE = 115200
OUTPUT_FILE = 'data.csv'

serialio.run_forever(COMPORT, BAUDRATE, OUTPUT_FILE)
