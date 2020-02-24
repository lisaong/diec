#!/usr/bin/env bash
docker run -it --privileged \
    -v $HOME/diec:/code \
    lisaong/rpi-buster-tf2.0-pyserial:1.1
