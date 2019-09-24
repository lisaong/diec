# This is the code we will run on the Raspberry Pi

# import helper classes for acquiring data from the Micro:bit
import sys
sys.path.append('..')
import serialio

import argparse
import tensorflow as tf
import tensorflow.keras as keras

class OnlineTrainer(serialio.SerialIoBase):
    def __init__(self, *args, **kw):
        '''https://github.com/pyserial/pyserial-asyncio/issues/41
        '''
        super().__init__(*args, **kw)

    def data_available(self, timestamp, data):
        """Overrides SerialIoBase.data_available()
        """
        #self.file.write(data)
        #self.file.write('\n')
        #self.file.flush()

parser = argparse.ArgumentParser(description='Online training using data from micro:bit')
parser.add_argument('comport', help='serial port for micro:bit')
args = parser.parse_args()
#print(args.comport)

