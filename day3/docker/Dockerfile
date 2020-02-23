FROM resin/rpi-raspbian:buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential git

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python3-pip python3-setuptools \
        python3-numpy python3-sklearn python3-pandas \
        libatlas-base-dev

# tensorflow needs libhdf5
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libhdf5-dev python3-h5py

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install tensorflow for python 3.7 raspberry pi 3
RUN curl -L -O https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.0.0/tensorflow-2.0.0-cp37-none-linux_armv7l.whl \
    && pip3 --no-cache-dir install \
            tensorflow-2.0.0-cp37-none-linux_armv7l.whl

RUN pip3 --no-cache-dir install \
         Cython==0.28.5 \
         scikit-learn==0.22

WORKDIR "/code"

# Test
RUN python3 -c "import tensorflow as tf; print('tensorflow', tf.__version__); \
     import sklearn; print('scikit-learn', sklearn.__version__);"
