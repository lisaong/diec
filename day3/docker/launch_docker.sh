#!/usr/bin/env bash
docker run -u $(id -u):$(id -g) -it \
    -v ~/diec:/code \
    lisaong/rpi-buster-tf2.0:1.0
