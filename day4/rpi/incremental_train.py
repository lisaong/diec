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

# parallelise collection and training
from dask import compute, delayed

class OnlineTrainer(serialio.SerialIoBase):
    def __init__(self, *args, **kw):
        '''https://github.com/pyserial/pyserial-asyncio/issues/41
        '''
        super().__init__(*args, **kw)

    def data_available(self, timestamp, data):
        """Overrides SerialIoBase.data_available()
        """
        #self.file.write(data)
        #self.file.write('\n')
        #self.file.flush()

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

def update_model(model, preprocessors_and_data, X, y):
    """Updates a model using the input data
    """
    timesteps = 20
    X_scaled = preprocessors_and_data['scaler'].transform(X)

    X_train = create_windows(X_scaled, timesteps)
    y_train = create_rolling_average(y, timesteps)

    X_val = preprocessors_and_data['X_val']
    y_val = preprocessors_and_data['y_val']

    model.fit(X_train, y_train, epochs=1, validation_data=(X_val, y_val))

parser = argparse.ArgumentParser(description='Online training using data from micro:bit')
parser.add_argument('comport', help='serial port for micro:bit')
args = parser.parse_args()
#print(args.comport)

# A model trained using Keras with Tensorflow backend can be
# loaded using tensorflow.keras
# This avoids having to compile and install Keras on the Raspberry Pi 
checkpoint = keras.models.load_model('./cnn_online.h5')
print(checkpoint.summary())

for_training = pickle.load(open('./preprocessors_and_data.pkl', 'rb'))

# temp
import pandas as pd
df_test = pd.read_csv('../data.csv', names=['Gesture', 'AccX', 'AccY', 'AccZ', 'Heading'])

timesteps = 20
sample = df_test.iloc[-(timesteps*2):]
X_sample = sample.loc[:, sample.columns != 'Gesture'].values
y_sample = np.where(sample['Gesture'], 1, 0)
# end temp

update_model(checkpoint, for_training, X_sample, y_sample)

