import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras.models
from keras.layers.convolutional import Conv1D, Conv2D, ZeroPadding1D, ZeroPadding2D
from keras.layers import Embedding
from keras.utils import plot_model
from math import floor, ceil


def load_data():
    dataset = 'train/1'
    calcium_train = pd.read_csv(dataset + '.train.calcium.csv')['0']  # todo: concat these
    spikes_train = pd.read_csv(dataset + '.train.spikes.csv')['0']
    return calcium_train, spikes_train

def plot(calcium, spikes, xlim):
    t = np.arange(len(calcium)) / 100.0
    plt.figure(figsize=(15, 3))
    plt.plot(t, calcium, color=(.1, .6, .4))
    plt.plot(t, spikes / 2.0 - 1, color='k')
    plt.yticks([])
    plt.ylim([-2., 4.])
    plt.xlim(xlim)
    plt.grid()
    plt.show()


x, y = load_data()
N = len(x)
x = x.values.reshape((1, N, 1))
y = y.values.reshape((1, N, 1))
# print(max(y))
# plot(x, y, [0, 100])
# print(max(y))
# training with tf


# create model
max_features = 10
embedding_dims = 10
maxlen = 100
epochs = 20
kernel_size = 5
pad_size = floor(kernel_size / 2)
model = keras.models.Sequential()
model.add(ZeroPadding1D(padding=pad_size, input_shape=(N, 1)))
model.add(Conv1D(filters=1, kernel_size=kernel_size))

# model.add(Dense(12, input_dim=8, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

# compile model
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

# fit the model
print('fitting...')
model.fit(x, y, epochs=epochs)

# evaluate the model
print('evaluating...')
scores = model.evaluate(x, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
