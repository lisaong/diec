/* Copyright 2018 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
#include <cstdio>
#include "tensorflow/lite/interpreter.h"
#include "tensorflow/lite/kernels/register.h"
#include "tensorflow/lite/model.h"
#include "tensorflow/lite/optional_debug_tools.h"

#include <vector>
#include "datasource.h"

// This is an example that is minimal to read a model
// from disk and perform inference. There is no data being loaded
// that is up to you to add as a user.
//
// Usage: minimal <tflite model>

// Custom operator declarations
TfLiteRegistration* Register_RandomStandardNormal();

#define TFLITE_MINIMAL_CHECK(x)                              \
  if (!(x)) {                                                \
    fprintf(stderr, "Error at %s:%d\n", __FILE__, __LINE__); \
    exit(1);                                                 \
  }

void fill_input_buffers(const tflite::Interpreter* interpreter){
  auto inputs = interpreter->inputs();
  TFLITE_MINIMAL_CHECK(inputs.size() == 1); // 1 input

  const int input_index = inputs[0];
  auto input_shape = interpreter->tensor(input_index)->dims;
  TFLITE_MINIMAL_CHECK(input_shape->data[1] == 50); // (batch_size, 50)

  // Read first few rows of data
  std::vector<float> data = datasource::GetData(/*rows=*/1);

  // Should not need this cast according to interpreter.h
  float* input = const_cast<float*>(interpreter->typed_input_tensor<float>(input_index));

  // Fill `input`
  std::memcpy(reinterpret_cast<void*>(input), data.data(),
      data.size() * sizeof(float));
}

int main(int argc, char* argv[]) {
  if(argc != 2) {
    fprintf(stderr, "minimal <tflite model>\n");
    return 1;
  }
  const char* filename = argv[1];

  // Load model
  std::unique_ptr<tflite::FlatBufferModel> model =
      tflite::FlatBufferModel::BuildFromFile(filename);
  TFLITE_MINIMAL_CHECK(model != nullptr);

  // Build the interpreter
  tflite::ops::builtin::BuiltinOpResolver resolver;

  // Register custom operators
  resolver.AddCustom("RandomStandardNormal",
      Register_RandomStandardNormal());

  tflite::InterpreterBuilder builder(*model, resolver);
  std::unique_ptr<tflite::Interpreter> interpreter;
  builder(&interpreter);
  TFLITE_MINIMAL_CHECK(interpreter != nullptr);

  // printf("=== Pre-allocate Interpreter State ===\n");
  // tflite::PrintInterpreterState(interpreter.get());

  // Allocate tensor buffers.
  TFLITE_MINIMAL_CHECK(interpreter->AllocateTensors() == kTfLiteOk);

  printf("=== Pre-invoke Interpreter State ===\n");
  tflite::PrintInterpreterState(interpreter.get());

  // Fill input buffers
  fill_input_buffers(interpreter.get());

  // Run inference
  TFLITE_MINIMAL_CHECK(interpreter->Invoke() == kTfLiteOk);
  printf("\n\n=== Post-invoke Interpreter State ===\n");
  tflite::PrintInterpreterState(interpreter.get());

  // Read output buffers
  const int output_index = interpreter->outputs()[0];
  auto output_dims = interpreter->tensor(output_index)->dims;
  float* output = interpreter->typed_output_tensor<float>(0);

  return 0;
}
