#!/usr/bin/env bash
docker run -it --privileged \
    -v ~/diec:/code \
    -e IOTA_TANGLE_URL=${IOTA_TANGLE_URL} \
    lisaong/rpi-buster-pyota:1.0
