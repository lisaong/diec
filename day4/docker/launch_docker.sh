#!/usr/bin/env bash
docker run -it --privileged \
    -v ~/diec:/code \
    lisaong/rpi-buster-tf1.14-pyserial:1.0
