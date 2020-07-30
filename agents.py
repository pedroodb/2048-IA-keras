from enviroment import Enviroment
import random

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
                print("You earned ", reward, ", total score: ", self.env.score)
        print('\nYou lost, final score: ', self.env.score)

class RandomAgent:

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
            movement = random.randint(0,3)
            reward, state, done = self.env.step(movement)
            self.print_matrix(state)
            print("You earned ", reward, ", total score: ", self.env.score)
        print('\nYou lost, final score: ', self.env.score)