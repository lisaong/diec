# Compiling TensorFlow Lite for Raspberry Pi

Reference: https://www.tensorflow.org/lite/guide/build_rpi

From an Ubuntu machine (with docker installed):

```
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
git checkout tags/v1.13.1 -b v1.13.1

sudo docker pull tensorflow/tensorflow:devel
sudo docker run -v /home/diec/tensorflow:/tensorflow -it tensorflow/tensorflow:devel bash
```

From the container:
```
sudo apt-get update
sudo apt-get install crossbuild-essential-armhf
cd /tensorflow
./tensorflow/lite/tools/make/download_dependencies.sh
./tensorflow/lite/tools/make/build_rpi_lib.sh
```

Compiled libraries are in `tensorflow/lite/tools/make/gen/rpi_armv71`
