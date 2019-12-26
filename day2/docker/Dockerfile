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
        libffi-dev \
        libssl-dev \
        mosquitto-clients \
        python3-dev \
        python3-pip \
        python3-setuptools

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/

RUN pip3 --no-cache-dir install \
    -r /tmp/requirements.txt

WORKDIR "/code"

# Test
RUN python3 -c "import iota; print('iota', iota.__version__);"
