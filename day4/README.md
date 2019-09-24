# Online Training on Raspberry Pi using TensorFlow

This example performs online training of a gesture detector on a Raspberry Pi,
using live sensor readings from a BBC Micro:bit.

1. Collect data from micro:bit
2. Train initial model using Google Colab, save a model checkpoint
3. Load model checkpoint on a Raspberry Pi
4. Continue training on the Raspberry Pi, using live sensor data from the micro:bit

## Micro:bit Programming
Using the [Python Micro:bit Editor](https://python.microbit.org/v/1.1), flash a micro:bit with [microbit/device_code.py](microbit/device_code.py)

## Initial data collection
In this section, you will collect data for your own micro:bit gesture.

1. Find the serial port path associated with micro:bit

   a. With the micro:bit **disconnected**:

       On MacOS, use `ls /dev/cu.*`

       On Windows, open Device Manager and expand "Ports (COM & LPT)"

   b. Connect the micro:bit:

       On MacOS, use `ls /dev/cu.*`, you should see a path that looks similar to `/dev/cu.usbmodemXXXX`

       On Windows, a new COMXX node should appear under "Ports (COM & LPT)"
   
2. Edit acquire_data.py, update comport to the path found in step 1:

   On MacOS:
    ```
    comport = '/dev/cu.usbmodem144102' # Example MacOS path
    ```

   On Windows:
    ```
    comport = 'COM3' # Example Windows path
    ```

3. Setup the data collection script
    ```
    conda activate diec
    conda install pyserial-asyncio
    ```

4. Run the data collection script. 
    ```
    python acquire_data.py
    ```
   As the script is running:
      - press button A to perform the gesture (by moving the micro:bit)
      - release button A when your gesture completes
      - repeat about 10 times to gather enough data

   Data will be saved to `data.csv`

## Training
1. Open notebook from Google Colab: [edge_online_learning.ipynb](edge_online_learning.ipynb)
2. Make a copy of the notebook
3. Upload data.csv to your Colab storage
4. Run each cell of the notebook, step by step
5. Download *.pkl and *.h5 from Colab storage to your laptop

## Online Learning
1. Deploy the *.pkl and *.h5 files to the Raspberry Pi. You can use [WinSCP](https://winscp.net/eng/download.php) (on Windows) or scp (on MacOS) to transfer files to the Raspberry Pi. You should copy the files to this folder:
```
~/diec/day4/rpi
``` 

2. Connect the Micro:bit device, check the serial path for it **from the docker container**.
```
ls /dev/ttyA*
```
Note down the serial path, e.g. `/dev/ttyACM0`

3. From the Raspberry Pi 3, launch docker container
```
cd ~/diec/day4/docker
sh ./launch_docker.sh
```
Note: the micro:bit must be connected **before** the docker container is launched, in order for the container to find the serial device.

4. From the **docker container** on the Raspberry Pi, verify that the serial device can be seen:
```
ls /dev/ttyA*
```

5. From the **docker container** on the Raspberry Pi, incrementally update the model after data has been acquired.
```
cd day4/rpi
python3 incremental_train.py /dev/ttyACM0 --update_interval=2
```
(Substitute `/dev/ttyACM0` with the path from step 3)