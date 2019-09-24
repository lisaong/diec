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

def create_windows(X):
    # ensure that dependencies are imported
    import numpy as np
  
    # convert the time series so that each entry contains a series of timesteps.
    # Before: rows, features
    # After: rows, timesteps, features
    timesteps = 20
    rolling_indexes = [(range(i, i+timesteps))
                     for i in range(X.shape[0]-timesteps)]

    X_out = np.take(X, rolling_indexes, axis=0)
    
    return X_out

def create_rolling_average(y):
    # compute y based on rolling average of window values
    # https://stackoverflow.com/questions/13728392/moving-average-or-running-mean
    timesteps = 20
    y_out = np.convolve(y, np.ones((timesteps,))/timesteps, mode='valid')

    # shift forward by 1
    y_out = y_out[1:]

    # apply a threshold to convert to 1 and 0
    y_out = np.where(y_out >= 0.5, 1, 0)

    return y_out

parser = argparse.ArgumentParser(description='Online training using data from micro:bit')
parser.add_argument('comport', help='serial port for micro:bit')
args = parser.parse_args()
#print(args.comport)

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

X_sample_scaled = for_training['scaler'].transform(X_sample)
X_sample_train = create_windows(X_sample_scaled)
y_sample_train = create_rolling_average(y_sample)

checkpoint.fit(X_sample_train, y_sample_train, epochs=1,
               validation_data=(for_training['X_val'], for_training['y_val']))