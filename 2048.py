import random
import copy


class Matrix:

    def __init__(self):
        self.matrix = [[1 for x in range(4)] for y in range(4)]
        self.score = 0
        self.add_tile()

    def equals(self, other_matrix):
        return self.matrix == other_matrix.matrix

    def print(self):
        for line in self.matrix:
            print([(tile if tile != 1 else 0) for tile in line])

    def move(self, direction):
        prev = copy.deepcopy(self)
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
        for (line_idx, line) in enumerate(self.matrix):
            joint = [False for i in range(4)]
            for i in range(2, -1, -1):
                if line[i] != 1:
                    for j in range(i, 3):
                        if line[j+1] == 1:
                            line[j+1] = line[j]
                            line[j] = 1
                        elif line[j+1] == line[j]:
                            if not joint[j+1]:
                                self.join((line_idx, j), (line_idx, j+1))
                                joint[j+1] = True
                                break
    
    def join(self, tile1, tile2):
        self.matrix[tile1[0]][tile1[1]] = 1
        self.matrix[tile2[0]][tile2[1]] *= 2
        self.score += self.matrix[tile2[0]][tile2[1]]

    def free_list(self):
        return [(i,j) for i in range(0, 4) for j in range(0, 4) if self.matrix[i][j] == 1]
        
    def add_tile(self):
        free_list = self.free_list()
        if free_list:
            coordinates = random.choice(free_list)
            self.matrix[coordinates[0]][coordinates[1]] = 2
            return True


class Game:

    matrix = Matrix()

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
            print('Invalid movement, try with w,a,s or d')

    def play(self):
        playing = True
        while playing:
            print("Score: ", self.matrix.score)
            self.matrix.print()
            print()
            movement = input()
            if self.move(movement):
                playing = self.matrix.add_tile()
        print('You lost')

g = Game()
g.play()