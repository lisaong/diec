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
#include "randomstandardnormal.h"
#include "model.h"

// This is an example that is minimal to read a model
// from disk and perform inference. There is no data being loaded
// that is up to you to add as a user.
//
// Usage: minimal <tflite model>

void PrintBuffer(const float *buffer, int rows, int columns)
{
    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < columns; ++j)
        {
            printf("%.4f ", buffer[i * columns + j]);
        }
        printf("\n");
    }
}

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        fprintf(stderr, "minimal <tflite model> <test data offset> <test data rows>\n");
        return 1;
    }
    const char *filename = argv[1];
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

    // Get data
    std::vector<float> data = datasource::GetData(offset, rows);

    // Fill input buffers
    float *input_buffer = nullptr;
    int input_rows, input_columns = 0;
    std::tie(input_buffer, input_rows, input_columns) = model::FillInputBuffer(
        interpreter.get(), data, rows);

    printf("\n\n=== Input (%d, %d) ===\n", input_rows, input_columns);
    PrintBuffer(input_buffer, input_rows, input_columns);

    printf("=== Pre-invoke Interpreter State ===\n");
    tflite::PrintInterpreterState(interpreter.get());

    // Run inference
    TFLITE_MINIMAL_CHECK(interpreter->Invoke() == kTfLiteOk);
    printf("\n\n=== Post-invoke Interpreter State ===\n");
    tflite::PrintInterpreterState(interpreter.get());

    // Read output buffers
    const float *output_buffer = nullptr;
    int output_rows, output_columns = 0;
    std::tie(output_buffer, output_rows, output_columns) = model::GetOutput(
        interpreter.get());

    printf("\n\n=== Output (%d, %d) ===\n", output_rows, output_columns);
    PrintBuffer(output_buffer, output_rows, output_columns);

    // Get the loss
    auto losses = model::Loss(interpreter.get());
    for (const auto &x : losses)
    {
        printf("%.4f ", x);
    }

    return 0;
}
