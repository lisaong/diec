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

4. Interpret the model file. This will load the .tflite model and perform an inference using a subset of windowed data from `test.csv`. 
```
./gen/bin/minimal ../models/converted_model.customops.tflite <offset> <num_rows>
```

For example:
```
pi@raspberrypi:~/diec/day3/inference $ gen/bin/minimal ../models/converted_model.customops.tflite 100 5

=== Input (5, 50) ===
1.0265 1.0573 1.0573 1.0287 0.9804 1.0419 1.0309 1.0375 1.0375 1.0419 1.0595 1.0595 1.0595 1.0507 1.0507 1.0419 1.0683 0.9541 0.9650 0.9650 0.9563 0.9563 1.0112 1.0112 0.9980 0.9475 1.0156 1.0551 1.0134 1.0134 0.9826 0.9541 0.9541 0.9804 0.9804 1.0375 1.0463 1.0617 1.0287 1.0287 1.0156 1.0156 1.0156 1.0507 1.0507 1.0485 1.0485 0.9760 0.9760 0.9694
1.0573 1.0573 1.0287 0.9804 1.0419 1.0309 1.0375 1.0375 1.0419 1.0595 1.0595 1.0595 1.0507 1.0507 1.0419 1.0683 0.9541 0.9650 0.9650 0.9563 0.9563 1.0112 1.0112 0.9980 0.9475 1.0156 1.0551 1.0134 1.0134 0.9826 0.9541 0.9541 0.9804 0.9804 1.0375 1.0463 1.0617 1.0287 1.0287 1.0156 1.0156 1.0156 1.0507 1.0507 1.0485 1.0485 0.9760 0.9760 0.9694 0.9650
1.0573 1.0287 0.9804 1.0419 1.0309 1.0375 1.0375 1.0419 1.0595 1.0595 1.0595 1.0507 1.0507 1.0419 1.0683 0.9541 0.9650 0.9650 0.9563 0.9563 1.0112 1.0112 0.9980 0.9475 1.0156 1.0551 1.0134 1.0134 0.9826 0.9541 0.9541 0.9804 0.9804 1.0375 1.0463 1.0617 1.0287 1.0287 1.0156 1.0156 1.0156 1.0507 1.0507 1.0485 1.0485 0.9760 0.9760 0.9694 0.9650 1.0068
1.0287 0.9804 1.0419 1.0309 1.0375 1.0375 1.0419 1.0595 1.0595 1.0595 1.0507 1.0507 1.0419 1.0683 0.9541 0.9650 0.9650 0.9563 0.9563 1.0112 1.0112 0.9980 0.9475 1.0156 1.0551 1.0134 1.0134 0.9826 0.9541 0.9541 0.9804 0.9804 1.0375 1.0463 1.0617 1.0287 1.0287 1.0156 1.0156 1.0156 1.0507 1.0507 1.0485 1.0485 0.9760 0.9760 0.9694 0.9650 1.0068 1.0068
0.9804 1.0419 1.0309 1.0375 1.0375 1.0419 1.0595 1.0595 1.0595 1.0507 1.0507 1.0419 1.0683 0.9541 0.9650 0.9650 0.9563 0.9563 1.0112 1.0112 0.9980 0.9475 1.0156 1.0551 1.0134 1.0134 0.9826 0.9541 0.9541 0.9804 0.9804 1.0375 1.0463 1.0617 1.0287 1.0287 1.0156 1.0156 1.0156 1.0507 1.0507 1.0485 1.0485 0.9760 0.9760 0.9694 0.9650 1.0068 1.0068 1.0068

=== Pre-invoke Interpreter State ===
Interpreter has 46 tensors and 14 nodes
Inputs: 29
Outputs: 6

Tensor   0 decoder/dense_3/MatMul_bias kTfLiteFloat32   kTfLiteMmapRo        100 bytes ( 0.0 MB)  25
Tensor   1 decoder/dense_3/Relu kTfLiteFloat32  kTfLiteArenaRw          4 bytes ( 0.0 MB)
Tensor   2 decoder/dense_4/MatMul_bias kTfLiteFloat32   kTfLiteMmapRo        100 bytes ( 0.0 MB)  25
Tensor   3 decoder/dense_4/Relu kTfLiteFloat32  kTfLiteArenaRw          4 bytes ( 0.0 MB)
Tensor   4 decoder/dense_5/BiasAdd kTfLiteFloat32  kTfLiteArenaRw          4 bytes ( 0.0 MB)
Tensor   5 decoder/dense_5/MatMul_bias kTfLiteFloat32   kTfLiteMmapRo        200 bytes ( 0.0 MB)  50
Tensor   6 decoder/dense_5/Sigmoid kTfLiteFloat32  kTfLiteArenaRw          4 bytes ( 0.0 MB)
Tensor   7 dense_1/kernel/transpose kTfLiteFloat32   kTfLiteMmapRo       5000 bytes ( 0.0 MB)  25 50
Tensor   8 dense_2/kernel/transpose kTfLiteFloat32   kTfLiteMmapRo       2500 bytes ( 0.0 MB)  25 25
Tensor   9 dense_3/kernel/transpose kTfLiteFloat32   kTfLiteMmapRo        600 bytes ( 0.0 MB)  25 6
Tensor  10 dense_4/kernel/transpose kTfLiteFloat32   kTfLiteMmapRo       2500 bytes ( 0.0 MB)  25 25
Tensor  11 dense_5/kernel/transpose kTfLiteFloat32   kTfLiteMmapRo       5000 bytes ( 0.0 MB)  50 25
Tensor  12 encoder/dense_1/MatMul_bias kTfLiteFloat32   kTfLiteMmapRo        100 bytes ( 0.0 MB)  25
Tensor  13 encoder/dense_1/Relu kTfLiteFloat32  kTfLiteArenaRw        500 bytes ( 0.0 MB)  5 25
Tensor  14 encoder/dense_2/MatMul_bias kTfLiteFloat32   kTfLiteMmapRo        100 bytes ( 0.0 MB)  25
Tensor  15 encoder/dense_2/Relu kTfLiteFloat32  kTfLiteArenaRw        500 bytes ( 0.0 MB)  5 25
Tensor  16 encoder/z/Exp        kTfLiteFloat32  kTfLiteArenaRw         24 bytes ( 0.0 MB)  1 6
Tensor  17 encoder/z/add        kTfLiteFloat32  kTfLiteArenaRw          4 bytes ( 0.0 MB)
Tensor  18 encoder/z/mul        kTfLiteFloat32  kTfLiteArenaRw        120 bytes ( 0.0 MB)  5 6
Tensor  19 encoder/z/mul_1      kTfLiteFloat32  kTfLiteArenaRw          4 bytes ( 0.0 MB)
Tensor  20 encoder/z/random_normal kTfLiteFloat32  kTfLiteArenaRw          4 bytes ( 0.0 MB)
Tensor  21 encoder/z/random_normal/RandomStandardNormal kTfLiteFloat32  kTfLiteDynamic          4 bytes ( 0.0 MB)
Tensor  22 encoder/z/random_normal/mean kTfLiteFloat32   kTfLiteMmapRo          4 bytes ( 0.0 MB)
Tensor  23 encoder/z/random_normal/mul kTfLiteFloat32  kTfLiteArenaRw          4 bytes ( 0.0 MB)
Tensor  24 encoder/z/random_normal/shape kTfLiteInt32   kTfLiteMmapRo          8 bytes ( 0.0 MB)  2
Tensor  25 encoder/z/random_normal/stddev kTfLiteFloat32   kTfLiteMmapRo          4 bytes ( 0.0 MB)
Tensor  26 encoder/z_log_var/MatMul_bias kTfLiteFloat32   kTfLiteMmapRo         24 bytes ( 0.0 MB)  6
Tensor  27 encoder/z_mean/BiasAdd kTfLiteFloat32  kTfLiteArenaRw        120 bytes ( 0.0 MB)  5 6
Tensor  28 encoder/z_mean/MatMul_bias kTfLiteFloat32   kTfLiteMmapRo         24 bytes ( 0.0 MB)  6
Tensor  29 encoder_input        kTfLiteFloat32  kTfLiteArenaRw       1000 bytes ( 0.0 MB)  5 50
Tensor  30 z_log_var/kernel/transpose kTfLiteFloat32   kTfLiteMmapRo        600 bytes ( 0.0 MB)  6 25
Tensor  31 z_mean/kernel/transpose kTfLiteFloat32   kTfLiteMmapRo        600 bytes ( 0.0 MB)  6 25
Tensor  32 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  33 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  34 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  35 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  36 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  37 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  38 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  39 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  40 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  41 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  42 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  43 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  44 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)
Tensor  45 (null)               kTfLiteNoType  kTfLiteMemNone          0 bytes ( 0.0 MB)  (null)

Node   0 Operator Builtin Code   9
  Inputs: 29 7 12
  Outputs: 13
Node   1 Operator Builtin Code   9
  Inputs: 13 8 14
  Outputs: 15
Node   2 Operator Builtin Code   9
  Inputs: 15 31 28
  Outputs: 27
Node   3 Operator Builtin Code   9
  Inputs: 15 30 26
  Outputs: 18
Node   4 Operator Custom Name RandomStandardNormal
  Inputs: 24
  Outputs: 21
Node   5 Operator Builtin Code  18
  Inputs: 21 25
  Outputs: 23
Node   6 Operator Builtin Code   0
  Inputs: 23 22
  Outputs: 20
Node   7 Operator Builtin Code  47
  Inputs: 18
  Outputs: 16
Node   8 Operator Builtin Code  18
  Inputs: 16 20
  Outputs: 19
Node   9 Operator Builtin Code   0
  Inputs: 27 19
  Outputs: 17
Node  10 Operator Builtin Code   9
  Inputs: 17 9 0
  Outputs: 1
Node  11 Operator Builtin Code   9
  Inputs: 1 10 2
  Outputs: 3
Node  12 Operator Builtin Code   9
  Inputs: 3 11 5
  Outputs: 4
Node  13 Operator Builtin Code  14
  Inputs: 4
  Outputs: 6

...

=== Output (5, 50) ===
0.9545 0.9480 0.9595 0.9590 0.9509 0.9432 0.9524 0.9427 0.9624 0.9447 0.9492 0.9439 0.9606 0.9520 0.9558 0.9486 0.9642 0.9551 0.9564 0.9587 0.9599 0.9620 0.9454 0.9527 0.9452 0.9479 0.9485 0.9582 0.9598 0.9499 0.9472 0.9668 0.9575 0.9524 0.9459 0.9534 0.9452 0.9407 0.9231 0.9357 0.9322 0.9185 0.9201 0.9056 0.9233 0.9002 0.8747 0.8918 0.8867 0.8793
0.9554 0.9488 0.9603 0.9598 0.9518 0.9440 0.9531 0.9439 0.9632 0.9455 0.9501 0.9449 0.9614 0.9529 0.9566 0.9496 0.9650 0.9562 0.9573 0.9593 0.9606 0.9627 0.9463 0.9536 0.9461 0.9489 0.9493 0.9592 0.9604 0.9509 0.9483 0.9674 0.9582 0.9535 0.9468 0.9542 0.9461 0.9418 0.9245 0.9369 0.9333 0.9197 0.9214 0.9072 0.9248 0.9018 0.8765 0.8935 0.8884 0.8813
0.9549 0.9481 0.9597 0.9593 0.9512 0.9434 0.9526 0.9432 0.9627 0.9448 0.9494 0.9442 0.9609 0.9523 0.9560 0.9489 0.9645 0.9557 0.9566 0.9588 0.9600 0.9621 0.9456 0.9530 0.9453 0.9482 0.9486 0.9586 0.9598 0.9502 0.9476 0.9669 0.9576 0.9529 0.9461 0.9537 0.9455 0.9410 0.9236 0.9361 0.9325 0.9189 0.9204 0.9064 0.9240 0.9007 0.8752 0.8926 0.8872 0.8800
0.9534 0.9464 0.9582 0.9577 0.9496 0.9419 0.9514 0.9410 0.9614 0.9431 0.9478 0.9421 0.9595 0.9506 0.9545 0.9469 0.9631 0.9538 0.9549 0.9576 0.9587 0.9608 0.9439 0.9514 0.9434 0.9463 0.9470 0.9569 0.9587 0.9483 0.9456 0.9657 0.9561 0.9509 0.9444 0.9522 0.9439 0.9389 0.9210 0.9340 0.9304 0.9169 0.9179 0.9035 0.9214 0.8978 0.8720 0.8897 0.8839 0.8761
0.9518 0.9448 0.9567 0.9561 0.9480 0.9404 0.9502 0.9388 0.9599 0.9416 0.9461 0.9401 0.9581 0.9490 0.9531 0.9450 0.9617 0.9519 0.9533 0.9566 0.9574 0.9595 0.9421 0.9496 0.9415 0.9444 0.9454 0.9550 0.9576 0.9465 0.9437 0.9645 0.9548 0.9489 0.9427 0.9509 0.9421 0.9369 0.9184 0.9318 0.9283 0.9147 0.9155 0.9005 0.9186 0.8951 0.8689 0.8866 0.8808 0.8723


```

### Debugging
This is useful for troubleshooting the custom operations.

```
make debug
gdb --args ./gen/bin/minimal ../models/converted_model.customops.tflite
```

https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf
