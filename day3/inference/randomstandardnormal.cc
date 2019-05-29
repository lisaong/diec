/* Implementation of the RandomStandardNormal custom operator

   https://www.tensorflow.org/lite/guide/ops_custom

   References:
       tensorflow/lite/kernels/sparse_to_dense.cc
*/

#include "tensorflow/lite/kernels/register.h"
#include "tensorflow/lite/kernels/kernel_util.h"
#include "tensorflow/lite/kernels/internal/tensor.h"

/* Outputs random values from a normal distribution.

  The generated values will have mean 0 and standard deviation 1.

  Arguments:
     shape: The shape of the output tensor.

  Returns A tensor of the specified shape filled with random normal values.
*/

using namespace tflite;

template <typename T>
TfLiteStatus Resize(TfLiteContext* context, const TfLiteTensor* output_shape,
                    TfLiteTensor* output) {
  const int output_dimensions = NumElements(output_shape);
  TfLiteIntArray* output_shape_array = TfLiteIntArrayCreate(output_dimensions);
  for (int i = 0; i < output_dimensions; ++i) {
    output_shape_array->data[i] = GetTensorData<T>(output_shape)[i];
  }

  return context->ResizeTensor(context, output, output_shape_array);
}

TfLiteStatus ResizeOutputShape(TfLiteContext* context,
                               const TfLiteTensor* output_shape,
                               TfLiteTensor* output) {
  if (output_shape->type == kTfLiteInt32) {
    return Resize<int32_t>(context, output_shape, output);
  } else if (output_shape->type == kTfLiteInt64) {
    return Resize<int64_t>(context, output_shape, output);
  } else {
    context->ReportError(context, "Shape type %d not supported.",
                         output_shape->type);
    return kTfLiteError;
  }
}

TfLiteStatus RandomStandardNormal_Prepare(TfLiteContext* context, TfLiteNode* node) {
  TF_LITE_ENSURE_EQ(context, NumInputs(node), 1);
  TF_LITE_ENSURE_EQ(context, NumOutputs(node), 1);

  const TfLiteTensor* shape = GetInput(context, node, 0);
  TfLiteTensor* output = GetOutput(context, node, 0);

  // Input will contain the shape of the output
  TF_LITE_ENSURE_EQ(context, NumDimensions(shape), 1);
  TF_LITE_ENSURE(context, shape->type == kTfLiteInt32 ||
                          shape->type == kTfLiteInt64);

  // Output shape is not known until Eval, postpone allocation
  SetTensorToDynamic(output);
  return kTfLiteOk;
}

TfLiteStatus RandomStandardNormal_Eval(TfLiteContext* context, TfLiteNode* node) {
  const TfLiteTensor* shape = GetInput(context, node, 0);
  TfLiteTensor* output = GetOutput(context, node, 0);

  TF_LITE_ENSURE_OK(context, ResizeOutputShape(context, shape, output));

  //float* output_data = output->data.f; // TODO: fix

  //for (size_t i=0; i<count; ++i) {
  //  output_data[i] = input_data[i];
  //}
  return kTfLiteOk;
}

TfLiteRegistration* Register_RandomStandardNormal() {
  static TfLiteRegistration r = {nullptr, nullptr, RandomStandardNormal_Prepare, RandomStandardNormal_Eval};
  return &r;
}
