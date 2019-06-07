/**
 * Declarations of input, output, and loss functions for the model
 */

#pragma once

#include <tuple>
#include <vector>
#include "tensorflow/lite/interpreter.h"

#define TFLITE_MINIMAL_CHECK(x)                              \
  if (!(x)) {                                                \
    fprintf(stderr, "Error at %s:%d\n", __FILE__, __LINE__); \
    exit(1);                                                 \
  }

namespace model
{
std::tuple<float * /*data*/, int /*rows*/, int /*columns*/> FillInputBuffer(
    tflite::Interpreter *interpreter,
    const std::vector<float> &data, int rows);

std::tuple<float* /*data*/, int /*rows*/, int /*columns*/> GetOutput(
    const tflite::Interpreter* interpreter);

std::vector<float> Loss(tflite::Interpreter* interpreter);

}