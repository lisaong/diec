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

void FillInputBuffers(tflite::Interpreter* interpreter,
  int offset, int rows){

  auto inputs = interpreter->inputs();
  TFLITE_MINIMAL_CHECK(inputs.size() == 1); // 1 input

  auto input_shape = interpreter->tensor(inputs[0])->dims; // (batch_size, 50)
  const auto batch_size = input_shape->data[0];
  const auto columns = input_shape->data[1];
  TFLITE_MINIMAL_CHECK(columns == 50);

  // Read data
  std::vector<float> data = datasource::GetData(offset, rows);

  if (rows != batch_size) {
    // Resize input tensor to match input batch size
    interpreter->ResizeInputTensor(inputs[0], {rows, columns});

    // Reallocate all tensors to match input batch size
    interpreter->AllocateTensors();
  }

  // Note: typed_input_tensor() uses an indexing from 0 to inputs().size(), not
  // the subgraph's tensor index
  // Should not need this cast according to interpreter.h
  auto input = const_cast<float*>(interpreter->typed_input_tensor<float>(0));

  printf("\n\n=== Input (%d, %d) ===\n", rows, columns);
  int i = 0;
  for (const auto &x : data){
     printf("%.4f ", x);
     if (++i % columns == 0) {
        printf("\n");
     }
  }
  printf("\n");

  // Fill `input`
  std::memcpy(reinterpret_cast<void*>(input), data.data(),
     data.size() * sizeof(float));
}

void PrintOutput(const tflite::Interpreter* interpreter){
  auto outputs = interpreter->outputs();
  TFLITE_MINIMAL_CHECK(outputs.size() == 1); // 1 output

  auto output_shape = interpreter->tensor(outputs[0])->dims;
  const auto rows = output_shape->data[0];
  const auto columns = output_shape->data[1];
  TFLITE_MINIMAL_CHECK(columns == 50);

  auto output = interpreter->typed_output_tensor<float>(0);

  printf("\n\n=== Output (%d, %d) ===\n", rows, columns);
  for (int i=0; i<rows; ++i) {
    for (int j=0; j<columns; ++j) {
     printf("%.4f ", output[j]);
    }
    printf("\n");
  }
}

int main(int argc, char* argv[]) {
  if(argc != 4) {
    fprintf(stderr, "minimal <tflite model> <test data offset> <test data rows>\n");
    return 1;
  }
  const char* filename = argv[1];
  const int offset = atoi(argv[2]);
  const int rows = atoi(argv[3]);

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

  // Allocate tensor buffers.
  TFLITE_MINIMAL_CHECK(interpreter->AllocateTensors() == kTfLiteOk);

  // Fill input buffers
  FillInputBuffers(interpreter.get(), offset, rows);

  printf("=== Pre-invoke Interpreter State ===\n");
  tflite::PrintInterpreterState(interpreter.get());

  // Run inference
  TFLITE_MINIMAL_CHECK(interpreter->Invoke() == kTfLiteOk);
  printf("\n\n=== Post-invoke Interpreter State ===\n");
  tflite::PrintInterpreterState(interpreter.get());

  // Read output buffers
  PrintOutput(interpreter.get());

  return 0;
}
