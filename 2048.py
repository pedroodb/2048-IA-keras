import random
import copy


class Enviroment:

    def __init__(self):
        self.matrix = [[1 for x in range(4)] for y in range(4)]
        self.score = 0
        self.add_tile()

    def step(self, action):
        reward = - self.score
        if self.move(action):
            self.add_tile()
        return (reward + self.score), self.matrix, self.locked()
        # return reward, state, done

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
        
    def add_tile(self):
        free_list = self.free_list()
        if free_list:
            coordinates = random.choice(free_list)
            self.matrix[coordinates[0]][coordinates[1]] = 2

    def locked(self):
        clone = copy.deepcopy(self)
        for direction in range(4):
            if clone.move(direction): return False
        return True
            
    def join(self, tile1, tile2):
        self.matrix[tile1[0]][tile1[1]] = 1
        self.matrix[tile2[0]][tile2[1]] *= 2
        self.score += self.matrix[tile2[0]][tile2[1]]

    def free_list(self):
        return [(i,j) for i in range(0, 4) for j in range(0, 4) if self.matrix[i][j] == 1]

    def equals(self, other_matrix):
        return self.matrix == other_matrix.matrix


class InteractiveAgent:

    directions = {
        'd': 0,
        'w': 1,
        'a': 2,
        's': 3,
    }

    def __init__(self):
        self.env = Enviroment()

    def print_matrix(self, matrix):
        for line in matrix:
            print([(tile if tile != 1 else 0) for tile in line])

    def play(self):
        done = False
        self.print_matrix(self.env.matrix)
        print()
        while not done:
            movement = InteractiveAgent.directions.get(input())
            if movement == None:
                print('Invalid movement, try with w, a, s or d')
            else:
                reward, state, done = self.env.step(movement)
                self.print_matrix(state)
                print("You earned ", reward)
        print('You lost')

g = InteractiveAgent()
g.play()