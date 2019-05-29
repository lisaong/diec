## Performing TensorFlow Lite Inference on Raspberry Pi

This example demonstrates:
- How the minimal.cc TensorFlow Lite example can be built using a Makefile instead of the Bazel build system.
- How to implement a custom operator and register it with the TensorFlow Lite kernel.

### Why not Python?
The benefits of the C++ API (compared to the Python API) are flexibility, lower overhead, smaller footprint, and portability to microcontrollers. In particular, custom operators take more work to expose through Python.

### References:
- https://www.tensorflow.org/lite/guide/inference#running_a_model
- https://www.tensorflow.org/lite/guide/ops_custom

### Instructions
From a Raspberry Pi:
1. Ensure that build essentials is installed
```
sudo apt-get install build-essential
```
2. C++ requires both the library (.a) and header files to compile. To get the header files, we will clone TensorFlow Lite and download dependencies (such as flatbuffers). Do this from the `day3/tf` folder
```
cd tf
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
git checkout tags/v1.13.1 -b v1.13.1
./tensorflow/lite/tools/make/download_dependencies.sh
cd ../../
```
3. Compile the executable
```
cd inference
make
```

4. Interpret the model file
```
./gen/bin/minimal ../models/converted_model.customops.tflite
```

### Debugging
This is useful for troubleshooting the custom operation.

```
make debug
gdb --args ./gen/bin/minimal ../models/converted_model.customops.tflite
```

https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf
