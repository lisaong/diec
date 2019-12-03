# Time Series Classification on Raspberry Pi using TensorFlow Lite

This example predicts a value using time series data from a Smart Factory.

1. Train model using Google Colab
2. Convert model to compressed version for Tensorflow Lite
3. Perform Inference on a Raspberry Pi using Tensorflow Lite

Dataset: https://www.kaggle.com/inIT-OWL/versatileproductionsystem

Overview:
![Workflow](https://www.tensorflow.org/lite/images/convert/workflow.svg)

## Training and TFLite Compression
1. Open notebook from Google Colab: [edge_time_series_classification.ipynb](edge_time_series_classification.ipynb)
2. Make a copy of the notebook
3. Run each cell of the notebook, step by step
4. Download *.pkl and *.tflite from Colab storage to your laptop

## Inference
This phase uses the TensorFlow Lite Python API to perform inference using your compressed TF Lite model.

Documentation: https://www.tensorflow.org/lite/guide/inference#running_a_model

1. Deploy the *.pkl and *.tflite files to the Raspberry Pi. You can use [WinSCP](https://winscp.net/eng/download.php) (on Windows) or scp (on MacOS) to transfer files to the Raspberry Pi. You should copy the files to this folder:
```
~/diec/day3/rpi
``` 
2. From the Raspberry Pi 3, launch docker image containing Tensorflow 2.0 for Python 3.7
```
cd ~/diec/day3/docker
sh ./launch_docker.sh
```
3. From the **docker container** running on the Raspberry Pi 3, evaluate the saved TF Lite model using inputs
```
cd day3/rpi
python3 evaluate.py input_file
```
