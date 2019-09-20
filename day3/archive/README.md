# Anomaly Detection on Raspberry Pi using TensorFlow Lite

This example trains a Variational Auto Encoder to detect anomalies on Smart Factory data.

1. Train model using Keras on a Desktop machine
2. Convert to compressed floating point version using Tensorflow Lite
3. Perform Inference on a Raspberry Pi 3

Dataset: https://www.kaggle.com/inIT-OWL/versatileproductionsystem

Overview:
![Workflow](https://www.tensorflow.org/lite/images/convert/workflow.svg)

## Training
This phase performs the training (using optional GPU).

See [Anomaly_detection_VAE.ipynb](Anomaly_detection_VAE.ipynb)

## Conversion
This phase takes a Keras model (HDF5 format) and converts it to a TensorFlow Lite model (.tflite)

See [Anomaly_detection_VAE.ipynb](Anomaly_detection_VAE.ipynb)

## Inference
This phase uses the TensorFlow Lite C++ API to perform inferences. We use the C++ API because the model contains a custom operator that is not natively supported by the core TensorFlow Lite Kernel.

### Compiling TensorFlow Lite library for Raspberry Pi

https://www.tensorflow.org/lite/guide/build_rpi

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

### Inference

See [inference/README.md](inference/README.md)