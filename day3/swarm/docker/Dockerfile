FROM balenalib/raspberrypi3:buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends --fix-missing \
        build-essential git \
        cmake libboost-all-dev

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python3-pip python3-setuptools \
        python3-numpy python3-scipy

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR "/code"

