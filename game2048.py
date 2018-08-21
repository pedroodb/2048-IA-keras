import random
import math


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
        direction = self.get_direction(move)
        if direction != -1:
            return self.matrix.move(direction)
        else:
            print('Invalid movement, try with w,a,s or d (hola soy Juan)'
                  '')

    def print_matrix(self):
        self.matrix.print()

    def play(self):
        playing = True
        while playing:
            self.print_matrix()
            movement = input()
            f = Formater()
            if self.get_direction(movement) != -1:
                self.save_to_file(f.format(self.matrix.matrix), self.get_direction(movement))
            if self.move(movement):
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