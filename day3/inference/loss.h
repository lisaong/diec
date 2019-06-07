/* Loss function declaration
*/

#pragma once

#include <vector>
#include "tensorflow/lite/interpreter.h"

std::vector<float> VaeLoss(tflite::Interpreter* interpreter);