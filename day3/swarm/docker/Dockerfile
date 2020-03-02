# https://esa.github.io/pygmo/install.html

# Build stage
FROM balenalib/raspberrypi3:buster as builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends --fix-missing \
        build-essential git

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python3-pip python3-setuptools \
        cmake \
        libboost-all-dev

RUN curl -L -O https://github.com/abhiTronix/TBB_Raspberry_pi/raw/master/libtbb-dev_4.5-1_armhf.deb \
    && dpkg -i libtbb-dev_4.5-1_armhf.deb \
    && ldconfig

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# https://esa.github.io/pagmo2/install.html
WORKDIR /tmp
RUN git clone https://github.com/esa/pagmo2.git
WORKDIR /tmp/pagmo2

# https://www.theimpossiblecode.com/blog/intel-tbb-on-raspberry-pi/
RUN  mkdir build /app && \
    cd build && \
    cmake ../ -DCMAKE_INSTALL_PREFIX=/app -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_CXX_FLAGS="-DTBB_USE_GCC_BUILTINS=1 -D__TBB_64BIT_ATOMICS=0" && \
    cmake --build . && \
    cmake --build . --target install

WORKDIR /app

RUN pip3 install --no-cache-dir \
      virtualenv

# https://pybind11.readthedocs.io/en/master/basics.html
RUN git clone https://github.com/pybind/pybind11.git && \
    cd pybind11 && \
    python3 setup.py install

RUN virtualenv . && \
     . bin/activate && \
     pip3 install --no-cache-dir \
       cloudpickle \
       dill \
       matplotlib \
       numpy

# https://esa.github.io/pygmo2/install.html
WORKDIR /tmp
RUN git clone https://github.com/esa/pygmo2.git
WORKDIR /tmp/pygmo2
RUN  mkdir build && \
    cd build && \
    /app/bin/activate && \
    cmake ../ -DCMAKE_INSTALL_PREFIX=/app/pybind11 -DCMAKE_BUILD_TYPE=Release \
    cmake --build . && \
    cmake --build . --target install

WORKDIR /app
RUN . bin/activate && \
    python3 -c "import pygmo; pygmo.test.run_test_suite()"

# Production stage
# FROM balenalib/raspberrypi3:buster
#COPY --from=builder /install /install

#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#        python3-dev python3-pip python3-setuptools \
#        libboost-all-dev

#RUN curl -L -O https://github.com/abhiTronix/TBB_Raspberry_pi/raw/master/libtbb-dev_4.5-1_armhf.deb \
#    && dpkg -i libtbb-dev_4.5-1_armhf.deb \
#    && ldconfig

#RUN  apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

#WORKDIR /code

