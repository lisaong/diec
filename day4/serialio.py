#
# Serial Io Protocol classes for acquiring data from the Micro:bit
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

class SerialIoBase(asyncio.Protocol):
    """Base class for acquiring serial data from the Micro:bit
    """
    def connection_made(self, transport):
        """Implements asyncio.Protocol.connection_made()
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        self.transport = transport
        self.buffer = b''
        print('port opened', transport)

    def data_received(self, data):
        """Implements asyncio.Protocol.data_received
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        self.buffer = self.buffer + data
        if b'\r\n' in data:
            self.process_data()
            self.buffer = b''

    def connection_lost(self, exc):
        """Implements asyncio.Protocol.connection_lost
        https://docs.python.org/3/library/asyncio-protocol.html
        """
        print('port closed')
        self.transport.loop.stop()

    def process_data(self):
        """Decodes buffer and notifies that data is available
        for processing
        """
        timestamp = int(time.time() * 1000)
        try:
            data = self.buffer.decode().strip()
            if len(data) > 0:
                print(data)
                self.data_available(timestamp, data)
        except:
            # decoding error
            pass

    def data_available(self, timestamp, data):
        """Derived classes should override this to perform specific processing
        """
        pass

class SerialIoToFile(SerialIoBase):
    def __init__(self, output_file, *args, **kw):
        '''https://github.com/pyserial/pyserial-asyncio/issues/41
        '''
        super().__init__(*args, **kw)
        self.file = open(output_file, 'w+')

    def data_available(self, timestamp, data):
        """Overrides SerialIoBase.data_available()
        """
        self.file.write(data)
        self.file.write('\n')
        self.file.flush()

def run_loop_forever(comport, baudrate, protocol_factory):
    loop = asyncio.get_event_loop()
    try:
        coro = serial_asyncio.create_serial_connection(loop,
            protocol_factory, comport, baudrate)
        loop.run_until_complete(coro)
        loop.run_forever()
    finally:
        loop.close()