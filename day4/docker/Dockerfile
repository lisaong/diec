FROM lisaong/rpi-buster-tf2.0:1.0

RUN pip3 --no-cache-dir install \
            pyserial-asyncio \
            dask distributed

WORKDIR "/code"

# Test
RUN python3 -c "import asyncio; import serial_asyncio;"
