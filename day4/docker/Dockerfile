FROM lisaong/rpi-buster-tf1.14:1.0

RUN pip3 --no-cache-dir install \
            pyserial-asyncio

WORKDIR "/code"

# Test
RUN python3 -c "import asyncio; import serial_asyncio;"
