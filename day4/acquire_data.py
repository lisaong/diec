#
# Acquires data from micro:bit using serial IO
# Author: Lisa Ong, NUS/ISS
#

# import helper classes for acquiring data from the Micro:bit
import serialio

# Refer to the documentation below on how to find the serial port for the micro:bit
# https://support.microbit.org/support/solutions/articles/19000022103-outputing-serial-data-from-the-micro-bit-to-a-computer

comport = 'COM3' # Example Windows port
# comport = '/dev/cu.usbmodem144102' # Example MacOS port

baudrate = 115200
output_file = 'data1.csv'

def SerialIoToFile_Factory():
    return serialio.SerialIoToFile(output_file)

serialio.run_loop_forever(comport, baudrate, SerialIoToFile_Factory)
