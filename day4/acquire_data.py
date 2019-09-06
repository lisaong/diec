#
# Acquires data from micro:bit using serial IO
# Author: Lisa Ong, NUS/ISS
#

#%%
# conda install pyserial-asyncio
import time
import asyncio
import serial_asyncio

#%%

COMPORT = '/dev/cu.usbmodem144102'
#COMPORT = 'COM3'
BAUDRATE = 115200
OUTPUT_FILE = 'data.csv'

class SerialIo(asyncio.Protocol):
    def connection_made(self, transport):
        """Implements asyncio.Protocol.connection_made()
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        self.transport = transport
        self.buffer = b''
        print('port opened', transport)
        self.file = open(OUTPUT_FILE, 'w+')

    def data_received(self, data):
        """Implements asyncio.Protocol.data_received
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        self.buffer = self.buffer + data
        if b'\r\n' in data:
            self.append_data()
            self.buffer = b''

    def connection_lost(self, exc):
        """Implements asyncio.Protocol.connection_lost
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        print('port closed')
        self.transport.loop.stop()

    def append_data(self):
        timestamp = int(time.time() * 1000)
        try:
            data = self.buffer.decode().strip()
            if len(data) > 0:
                print(data)
                self.file.write(data)
                self.file.write('\n')
                self.file.flush()
        except:
            # decoding error
            pass

#%%
loop = asyncio.get_event_loop()
try:
    coro = serial_asyncio.create_serial_connection(loop, SerialIo,
        COMPORT, baudrate=BAUDRATE)
    loop.run_until_complete(coro)
    loop.run_forever()
finally:
    loop.close()


#%%
