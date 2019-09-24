#
# Serial Io Protocol module for acquiring data from the Micro:bit
# and saving data to a file
#
# Author: Lisa Ong, NUS/ISS
#
# Pre-requisites: pyserial-asyncio
#   `conda install pyserial-asyncio`, or `pip3 install pyserial-asyncio`
#
import time
import asyncio
import serial_asyncio

class SerialIoToFile(asyncio.Protocol):
    def __init__(self, output_file, *args, **kw):
        '''https://github.com/pyserial/pyserial-asyncio/issues/41
        '''
        super().__init__(*args, **kw)
        self.output_file = output_file

    def connection_made(self, transport):
        """Implements asyncio.Protocol.connection_made()
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        self.transport = transport
        self.buffer = b''
        print('port opened', transport)
        self.file = open(self.output_file, 'w+')

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

def run_forever(comport, baudrate, output_file):
    def SerialIoToFile_Factory():
        return SerialIoToFile(output_file)

    loop = asyncio.get_event_loop()
    try:
        coro = serial_asyncio.create_serial_connection(loop,
            SerialIoToFile_Factory, comport, baudrate)
        loop.run_until_complete(coro)
        loop.run_forever()
    finally:
        loop.close()