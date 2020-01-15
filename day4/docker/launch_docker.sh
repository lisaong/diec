#!/usr/bin/env bash
docker run -u $(id -u):$(id -g) -it --privileged \
    -v ~/diec:/code \
    lisaong/rpi-buster-tf2.0-pyserial:1.0
