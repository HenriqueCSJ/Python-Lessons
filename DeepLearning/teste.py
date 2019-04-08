import numpy as np

import pandas as pb
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets.samples_generator import make_circles

X, y = make_circles(n_samples=1000, shuffle=True,
                    noise=0.1, random_state=101, factor=0.2)

X.shape

plt.figure(figsize=(5,5))
plt.plot(X[y == 0, 0], X[y == 0, 1], "ob", alpha=0.5)
plt.plot(X[y == 1, 0], X[y == 1, 1], "xr", alpha=0.65)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.legend(["0", "1"])
plt.title("Blue circles and red crosses")

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

model = Sequential()

model.add(Dense(4, input_shape=(2,), activation="tanh"))
model.add(Dense(1, activation="sigmoid"))

model.compile(SGD())