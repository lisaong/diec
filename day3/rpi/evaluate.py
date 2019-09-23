# This is the code we will run on the Raspberry Pi
import pickle
import numpy as np
import tensorflow as tf
import argparse

def load_test_data(data_filename, preprocessors_filename):
  timesteps = 10

  # Load test numpy array and process it
  test_array = pickle.load(open(data_filename, 'rb'))

  preprocessors = pickle.load(open(preprocessors_filename, 'rb'))
  vt = preprocessors['variance_threshold']
  feature_scaler = preprocessors['feature_scaler']

  # select features
  test_X = vt.transform(test_array)

  # scale
  test_X_scaled = feature_scaler.transform(test_X)

  # create windowed
  rolling_indexes = [(range(i, i+timesteps))
                     for i in range(test_X_scaled.shape[0]-timesteps)]

  test_X_sequence = np.take(test_X_scaled, rolling_indexes, axis=0)
  print(test_X_sequence.shape) # (rows, timesteps, features)

  return test_X_sequence

def predict(model_path, test_data):
  # Load TFLite model and allocate tensors.
  interpreter = tf.lite.Interpreter(model_path=model_path)
  interpreter.allocate_tensors()

  # Get input and output tensors.
  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  # Test model on input data.
  input_shape = input_details[0]['shape']

  # Loop through each row of test_data and perform inference
  for i in range(test_data.shape[0]):

    # add batch dimension
    input_data = np.expand_dims(test_data[i], axis=0).astype('float32')

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(output_data)

# Download the following files from Colaboratory and copy to the Raspberry Pi:
#   *.pkl
#   cnn.tflite
#   evaluate.py

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str, help='path to pkl file containing input data')
args = parser.parse_args()

X_test = load_test_data(args.input, './preprocessors.pkl')
predict('./cnn.tflite', X_test)
