import random
import math


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
          epochs=200,
          batch_size=128)

score = model.evaluate(data, labels, batch_size=128)

class Matrix:

    matrix = [[0 for x in range(4)] for y in range(4)]

    def __init__(self):
        self.add_two()

    def clone(self):
        new_matrix = Matrix()
        for i in range(0, 4):
            for j in range(0, 4):
                new_matrix.matrix[i][j] = self.matrix[i][j]
        return new_matrix

    def equals(self, other_matrix):
        equals = True
        for i in range(0, 4):
            for j in range(0, 4):
                if other_matrix.matrix[i][j] != self.matrix[i][j]:
                    equals = False
        return equals

    def print(self):
        for i in self.matrix:
            print(i)

    def move(self, direction):
        prev = self.clone()
        for i in range(0, direction):
            self.rotate()
        self.move_right()
        for i in range(0, (4 - direction)):
            self.rotate()
        return not prev.equals(self)

    def rotate(self):
        self.matrix = list(zip(*self.matrix[::-1]))
        for i in range(0, 4):
            self.matrix[i] = list(self.matrix[i])

    def move_right(self):
        for line in self.matrix:
            for i in range(2, -1, -1):
                if line[i] != 0:
                    joint = False
                    for j in range(i, 3):
                        if line[j+1] == 0:
                            line[j+1] = line[j]
                            line[j] = 0
                        elif line[j+1] == line[j]:
                            if not joint:
                                line[j + 1] = (line[j]*2)
                                line[j] = 0
                                joint = True

    def free_list(self):
        free_list = list()
        for i in range(0, 4):
            for j in range(0, 4):
                if self.matrix[i][j] == 0:
                    free_list.append((i, j))
        return free_list

    def add_two(self):
        free_list = self.free_list()
        if free_list:
            coordinates = random.choice(free_list)
            self.matrix[coordinates[0]][coordinates[1]] = 2
            return True

class Game:

    matrix = Matrix()

    @staticmethod
    def save_to_file(matrix, movement):
        with open("matrix_history.txt", "a") as matrix_history:
            print(matrix, file=matrix_history)
        with open("movement_history.txt", "a") as movement_history:
            print(movement, file=movement_history)

    @staticmethod
    def get_direction(move):
        # Get a movement direction from w,a,s or d
        return {
            'd': 0,
            'w': 1,
            'a': 2,
            's': 3,
        }.get(move, -1)

    def move(self, move):
        direction = move
        if direction != -1:
            return self.matrix.move(direction)
        else:
            print('Invalid movement, try with w,a,s or d (hola soy Juan)'
                  '')

    def print_matrix(self):
        self.matrix.print()

    def shape_matrix(self):
        to_convert = []
        as_array = []
        for line in self.matrix.matrix:
            for i in line:
                as_array.append(i)
        to_convert.append(as_array)
        return np.asarray(to_convert)

    def play(self):
        playing = True
        while playing:
            self.print_matrix()
            movement_prediction = model.predict(self.shape_matrix()).tolist()[0]
            print(movement_prediction)
            movement = movement_prediction.index(max(movement_prediction))
            print(movement)
            while not self.move(movement):
                if all(i==0 for i in movement_prediction):
                    break
                movement_prediction[movement] = 0
                print(movement_prediction)
                movement = movement_prediction.index(max(movement_prediction))
            playing = self.matrix.add_two()
        print('You lost')


class Formater:

    def log(self, num):
        if num != 0:
            return int(math.log(num, 2))
        else:
            return 0

    def format(self, matrix):
        formated_str = ""
        for line in matrix:
            for i in line:
                formated_str += str(self.log(i))
        return formated_str

g = Game()
g.play()
