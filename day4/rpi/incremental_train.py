# This is the code we will run on the Raspberry Pi

# import helper classes for acquiring data from the Micro:bit
import sys
sys.path.append('..')
import serialio

import os
import argparse
import numpy as np
import pickle

from dask.distributed import Client, Queue

import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.callbacks import ModelCheckpoint

dask_client = Client(processes=False) # use threads
dask_queue = Queue() # ensure that training is executed sequentially

# Global model checkpoint accessed from the queue
# A workaround for a pickling issue in TF 2.0
#  https://github.com/tensorflow/tensorflow/issues/33283
checkpoint = None
save_model = None

def load_model():
    """manually creates a model and loads its weights, instead of using
    tensorflow.keras.load_model()

    A workaround for a pickling issue in TF 2.0
    https://github.com/tensorflow/tensorflow/issues/33283
    """

    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv1D, Flatten, Dense
    from tensorflow.keras.optimizers import SGD

    model = Sequential()

    model.add(Conv1D(64, kernel_size=3,
                    input_shape=(20, 4),
                    activation='relu'))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
        optimizer=SGD(learning_rate=.01), metrics=['acc'])
    model.load_weights("./cnn_online.h5")

    return model

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

        self.preprocessors_and_data = pickle.load(open(
            './preprocessors_and_data.pkl', 'rb'))

        self.timesteps = 20 # timesteps for windowing
        self.min_batch_size = self.timesteps * update_interval
        self.num_columns = 5 # number of data columns
        self.samples = np.array([]) # buffer to hold samples

    def data_available(self, timestamp, data):
        """Overrides SerialIoBase.data_available() to
        accumulate the data and update the model

        This implementation uses queuing to perform the
        model update in parallel to data acquisition.
        """
        try:
            # clean
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
                print(f'Queuing task to update model using {self.samples.shape} samples')

                dask_queue.put(dask_client.submit(
                    SerialIoUpdateModel.update_model,
                    self.timesteps,
                    self.preprocessors_and_data,
                    np.copy(self.samples)))

                self.samples = np.array([])

        except Exception as e:
            print(e)

    def update_model(timesteps, preprocessors_and_data, samples):
        """Updates a model using the input data
        """
        # Global model checkpoint
        # A workaround for a pickling issue in TF 2.0
        #  https://github.com/tensorflow/tensorflow/issues/33283
        global checkpoint
        global save_model

        print(f'Entering update_model with {samples.shape} samples')
        X = samples[:, 1:]
        X_scaled = preprocessors_and_data['scaler'].transform(X)
        X_train = create_windows(X_scaled, timesteps)

        y = samples[:, 0]
        y_train = create_rolling_average(y, timesteps)

        # saved validation set from original training
        # so that we can monitor whether model is overfitting
        X_val = preprocessors_and_data['X_val']
        y_val = preprocessors_and_data['y_val']

        # Initialise the global model checkpoint on demand
        # This assumes that Dask maintains thread affinity for its tasks
        if checkpoint is None:
            checkpoint = load_model()
            save_model = ModelCheckpoint('./cnn_online_updated_weights.h5',
                save_best_only=True, save_weights_only=True)

        checkpoint.fit(X_train, y_train, epochs=1, 
            validation_data=(X_val, y_val),
            callbacks=[save_model])

# main program
update_interval = 5
baudrate = 115200

parser = argparse.ArgumentParser(description='Online training using data from micro:bit')
parser.add_argument('comport', help='serial port for micro:bit')
parser.add_argument('--update_interval',
    help='minimum intervals of timesteps before doing a model update (must be at least 2)',
    default=update_interval)
args = parser.parse_args()

if args.update_interval:
    update_interval = int(args.update_interval)
    if update_interval < 2: # required by create_windows()
        raise parser.error('UPDATE_INTERVAL must be at least 2')

def SerialIoUpdateModel_Factory():
    return SerialIoUpdateModel(update_interval)

serialio.run_loop_forever(args.comport, baudrate, SerialIoUpdateModel_Factory)
