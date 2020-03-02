# https://esa.github.io/pygmo/install.html

# Builder
FROM balenalib/raspberrypi3:buster as builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends --fix-missing \
        build-essential git \
        cmake libboost-all-dev

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python3-pip python3-setuptools \
        python3-numpy python3-scipy

RUN curl -L -O https://github.com/abhiTronix/TBB_Raspberry_pi/raw/master/libtbb-dev_4.5-1_armhf.deb \
    && dpkg -i libtbb-dev_4.5-1_armhf.deb \
    && ldconfig

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN  git clone https://github.com/esa/pagmo.git
WORKDIR /app/pagmo

RUN  mkdir build /install \
    && cd build \
    && cmake ../ -DCMAKE_INSTALL_PREFIX=/install -DCMAKE_BUILD_TYPE=Release \
    && cmake --build . \
    && cmake --build . --target install

# Production
# FROM balenalib/raspberrypi3:buster

# WORKDIR "/code"

