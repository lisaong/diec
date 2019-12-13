FROM resin/rpi-raspbian:buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential git

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libssl-dev \
        mosquitto \
        mosquitto-clients \
        python3-pip

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install \
    virtualenv \
    && virtualenv -p python iota

COPY requirements.txt /tmp/

RUN source iota/bin/activate \
    && pip --no-cache-dir install \
    -r /tmp/requirements.txt

WORKDIR "/code"

# Test
RUN python3 -c "import pyota; print('pyota', pyota.__version__);"
