#!/usr/bin/env bash

# https://vsupalov.com/docker-arg-env-variable-guide/
docker run -it --privileged \
    -v ~/diec:/code \
    -e IOTA_TANGLE_URL=${IOTA_TANGLE_URL:-http://your_ec2_url:14265} \
    --env-file=.env \     
    lisaong/rpi-buster-pyota:1.0
