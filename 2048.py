import math
import random

class Matrix:

    def __init__(self):
        self.matrix = [[0 for _ in range(4)] for _ in range(4)]
        self.score = 0
        self.add_two()
        
    def reset(self):
        self.__init__()
    
    def status(self):
        return [i for line in self.matrix for i in line ]

    def step(self, move):
        self.move(move)
        return self.status(),self.score,self.add_two(),''

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
                                res = (line[j]*2)
                                line[j + 1] = res
                                self.score += res
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


a = Matrix()
while True:
    print(a.step(int(input())))