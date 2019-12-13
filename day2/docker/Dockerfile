# Consider: moving to balena
#   https://www.balena.io/docs/reference/base-images/base-images/
# FROM balenalib/raspberrypi3:buster
#
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

COPY requirements.txt /tmp/

RUN pip --no-cache-dir install \
    -r /tmp/requirements.txt

WORKDIR "/code"

# Test
RUN python3 -c "import pyota; print('iota', iota.__version__);"
