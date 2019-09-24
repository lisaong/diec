# This is the code we will run on the Raspberry Pi

# import helper classes for acquiring data from the Micro:bit
import sys
sys.path.append('..')
import serialio

import argparse
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import pickle
from dask.distributed import Client, Queue

def create_windows(X, timesteps):
    """convert the time series so that each entry contains a series of timesteps.
    Before: rows, features
    After: rows, timesteps, features
    """  
    rolling_indexes = [(range(i, i+timesteps))
                        for i in range(X.shape[0]-timesteps)]

    X_out = np.take(X, rolling_indexes, axis=0)

    return X_out

def create_rolling_average(y, timesteps):
    """compute y based on rolling average of window values
    https://stackoverflow.com/questions/13728392/moving-average-or-running-mean
    """
    y_out = np.convolve(y, np.ones((timesteps,))/timesteps, mode='valid')

    # shift forward by 1
    y_out = y_out[1:]

    # apply a threshold to convert to 1 and 0
    y_out = np.where(y_out >= 0.5, 1, 0)

    return y_out

class SerialIoUpdateModel(serialio.SerialIoBase):
    def __init__(self, update_interval, *args, **kw):
        '''https://github.com/pyserial/pyserial-asyncio/issues/41
        '''
        super().__init__(*args, **kw)

        # A model trained using Keras with Tensorflow backend can be
        # loaded using tensorflow.keras
        # This avoids having to compile and install Keras on the Raspberry Pi 
        self.checkpoint = keras.models.load_model('./cnn_online.h5')
        self.checkpoint.summary()

        self.preprocessors_and_data = pickle.load(open(
            './preprocessors_and_data.pkl', 'rb'))

        self.timesteps = 20 # timesteps for windowing
        self.min_batch_size = self.timesteps * update_interval
        self.num_columns = 5 # number of data columns
        self.samples = np.array([]) # buffer to hold samples

        self.dask_client = Client(processes=False) # use threads
        self.dask_queue = Queue()

    def data_available(self, timestamp, data):
        """Overrides SerialIoBase.data_available() to
        accumulate the data and update the model
        
        This implementation keeps things simple by performing the
        update sequentially to data acquisition.
        """
        try:
            # cleaning
            data = data.replace('\r\n', ',').replace('True', '1').replace('False', '0')
            data = np.array(data.split(',')).astype(np.float)

            # split into multiple rows
            data = data.reshape(-1, self.num_columns)

            # append to samples buffer
            if self.samples.shape[0] == 0:
                self.samples = data
            else:
                self.samples = np.vstack((self.samples, data))

            # once the minimum batch size is reached, queue a task
            # to update the model using a snapshot of the collected samples
            if self.samples.shape[0] >= self.min_batch_size:
                self.dask_queue.put(self.dask_client.submit(
                    self.update_model, 
                    self.samples.copy()))
                self.samples = np.array([])

        except Exception as e:
            print(e)

    def update_model(self, samples):
        """Updates a model using the input data
        """
        print(f'Updating model using {samples.shape[0]} samples')

        X = samples[:, 1:]
        X_scaled = self.preprocessors_and_data['scaler'].transform(X)
        X_train = create_windows(X_scaled, self.timesteps)
 
        y = samples[:, 0]
        y_train = create_rolling_average(y, self.timesteps)

        # saved validation set from original training
        # so that we can monitor whether model is overfitting
        X_val = self.preprocessors_and_data['X_val']
        y_val = self.preprocessors_and_data['y_val']

        self.checkpoint.fit(X_train, y_train, epochs=1, validation_data=(X_val, y_val))

# main program
update_interval = 5
baudrate = 115200

parser = argparse.ArgumentParser(description='Online training using data from micro:bit')
parser.add_argument('comport', help='serial port for micro:bit')
parser.add_argument('--update_interval',
    help='minimum intervals of timesteps before doing a model update',
    default=update_interval)
args = parser.parse_args()

if args.update_interval:
    update_interval = args.update_interval

def SerialIoUpdateModel_Factory():
    return SerialIoUpdateModel(args.update_interval)

serialio.run_loop_forever(args.comport, baudrate, SerialIoUpdateModel_Factory)
