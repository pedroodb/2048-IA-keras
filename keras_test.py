import numpy as np

def get_data(file_name):
    matrix_history = []
    matrix_line = []
    with open(file_name, "r") as mh:
        while True:
            c = mh.read(1)
            if not c:
                break
            elif c != '\n':
                matrix_line.append(int(c))
            else:
                matrix_history.append(matrix_line)
                matrix_line = []
    return np.asarray(matrix_history)

def get_labels(file_name):
    labels = []
    with open(file_name, "r") as l:
        while True:
            c = l.read(1)
            if not c:
                break
            elif c != '\n':
                label_line = [0, 0, 0, 0]
                label_line[int(c)] = 1
                labels.append(label_line)
    return np.asarray(labels)


data = get_data("matrix_history.txt")
labels = get_labels("movement_history.txt")

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=16))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(data, labels,
          epochs=5000,
          batch_size=128)

score = model.evaluate(data, labels, batch_size=128)

