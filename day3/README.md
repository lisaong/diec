# Anomaly Detection on Raspberry Pi using TensorFlow Lite

This example predicts a value using time series data from a Smart Factory.

1. Train model using Keras on a Desktop machine
2. Convert to compressed floating point version using Tensorflow Lite
3. Perform Inference on a Raspberry Pi

Dataset: https://www.kaggle.com/inIT-OWL/versatileproductionsystem

Overview:
![Workflow](https://www.tensorflow.org/lite/images/convert/workflow.svg)

## Training and Conversion
1. Go to http://colab.research.google.com
2. Open notebook from Github: [edge_time_series_classification.ipynb](edge_time_series_classification.ipynb)

## Inference
This phase uses the TensorFlow Lite Python API to perform inference using your compressed TF Lite model.

Documentation: https://www.tensorflow.org/lite/guide/inference#running_a_model

1. Run the Training notebook from Google Colab
2. Download *.pkl and *.tflite from Colab storage to your laptop
3. Deploy the files to the Raspberry Pi. You can use [WinSCP](https://winscp.net/eng/download.php) (on Windows) or scp (on MacOS) to transfer files to the Raspberry Pi.
4. From the Raspberry Pi 3, launch docker image containing Tensorflow 1.14 for Python 3.7
```
cd ~/diec/day3/docker
sh ./launch_docker.sh
```
5. From the docker instance running on the Raspberry Pi 3, evaluate the saved TF Lite model using inputs
```
cd /code/day3
python3 evaluate.py X_test.pkl
```
