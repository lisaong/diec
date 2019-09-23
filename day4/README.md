# Online Training on Raspberry Pi using TensorFlow

This example performs online training of a gesture detector on a Raspberry Pi,
using live sensor readings from a BBC Micro:bit.

1. Train initial model using Google Colab, save a model checkpoint
2. Load model checkpoint on a Raspberry Pi
3. Continue training on the Raspberry Pi using Tensorflow

## Training
1. Open notebook from Google Colab: [edge_online_learning.ipynb](edge_online_learning.ipynb)
2. Make a copy of the notebook
3. Run each cell of the notebook, step by step
4. Download *.pkl and *.h5 from Colab storage to your laptop

## Online Learning
1. Deploy the *.pkl and *.h5 files to the Raspberry Pi. You can use [WinSCP](https://winscp.net/eng/download.php) (on Windows) or scp (on MacOS) to transfer files to the Raspberry Pi. You should copy the files to this folder:
```
~/diec/day4/rpi
``` 
2. From the Raspberry Pi 3, launch docker image
```
cd ~/diec/day4/docker
sh ./launch_docker.sh
```
3. Connect the Micro:bit device, check the serial path for it **from the docker container**.
```
ls /dev/ttyA*
```
Note down the serial path, e.g. `/dev/ttyACM0`

4. From the **docker container** on the Raspberry Pi, incrementally update the model after data has been acquired.
```
cd /code/day4/rpi
python3 train.py /dev/ttyACM0
```
(Substitute `/dev/ttyACM0` with the path from step 3)