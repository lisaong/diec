#!/usr/bin/env bash

# https://vsupalov.com/docker-arg-env-variable-guide/
docker run -it --privileged \
    -v ~/diec:/code \
    --env-file=.env \
    lisaong/rpi-buster-pyota:1.0
