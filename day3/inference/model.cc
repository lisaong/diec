/**
 * Implements input, output, and loss calculation for the model
 */
#include "model.h"

namespace model
{

std::tuple<float * /*data*/, int /*rows*/, int /*columns*/> GetInputs(
    const tflite::Interpreter *interpreter)
{
    auto inputs = interpreter->inputs();
    TFLITE_MINIMAL_CHECK(inputs.size() == 1); // 1 input

    auto input_shape = interpreter->tensor(inputs[0])->dims; // (batch_size, 50)
    const auto batch_size = input_shape->data[0];
    const auto columns = input_shape->data[1];
    TFLITE_MINIMAL_CHECK(columns == 50);

    // Note: typed_input_tensor() uses an indexing from 0 to inputs().size(), not
    // the subgraph's tensor index
    // Should not need this cast according to interpreter.h 
    auto input_buffer = const_cast<float*>(interpreter->typed_input_tensor<float>(0));
    return std::make_tuple(input_buffer, batch_size, columns);
}

std::tuple<float * /*data*/, int /*rows*/, int /*columns*/> FillInputBuffer(
    tflite::Interpreter *interpreter,
    const std::vector<float> &data, int rows)
{
    float* input_buffer = nullptr;
    int batch_size, columns = 0;
    std::tie(input_buffer, batch_size, columns) = GetInputs(interpreter);

    if (rows != batch_size)
    {
        auto inputs = interpreter->inputs();

        // Resize input tensor to match input batch size
        interpreter->ResizeInputTensor(inputs[0], {rows, columns});

        // Reallocate all tensors to match input batch size
        interpreter->AllocateTensors();
    }

    // Fill `input`
    std::memcpy(reinterpret_cast<void *>(input_buffer), data.data(),
                data.size() * sizeof(float));

    return std::make_tuple(input_buffer, rows, columns);
}

std::tuple<float * /*data*/, int /*rows*/, int /*columns*/> GetOutputs(
    const tflite::Interpreter *interpreter)
{
    auto outputs = interpreter->outputs();
    TFLITE_MINIMAL_CHECK(outputs.size() == 1); // 1 output

    auto output_shape = interpreter->tensor(outputs[0])->dims;
    const auto rows = output_shape->data[0];
    const auto columns = output_shape->data[1];
    TFLITE_MINIMAL_CHECK(columns == 50);

    auto output_buffer = interpreter->typed_output_tensor<float>(0);
    return std::make_tuple(output_buffer, rows, columns);
}

/* Implementation of the loss function for VAE Anomaly Detection

    def vae_loss_func(x, x_true):
        reconstruction_loss = mse(x, x_true)
        reconstruction_loss *= self.original_dim
        kl_loss = 1 + self.z_log_var - K.square(self.z_mean) - K.exp(self.z_log_var)
        kl_loss = K.sum(kl_loss, axis=-1)
        kl_loss *= -0.5
        return K.mean(reconstruction_loss + kl_loss)
 */
std::vector<float> Loss(tflite::Interpreter *interpreter)
{
    return {};
}

} // namespace model