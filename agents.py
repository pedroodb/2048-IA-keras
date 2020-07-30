import random

class InteractiveAgent:

    directions = {
        'd': 0,
        'w': 1,
        'a': 2,
        's': 3,
    }

    def __init__(self, enviroment):
        self.env = enviroment

    def game(self):
        done = False
        self.env.render()
        print()
        while not done:
            movement = InteractiveAgent.directions.get(input())
            if movement == None:
                print('Invalid movement, try with w, a, s or d')
            else:
                obs, reward, done, _ = self.env.step(movement)
                self.env.render()
                print("You earned ", reward, ", total score: ", self.env.score)
        print('\nYou lost, final score: ', self.env.score)

class RandomAgent:

    def __init__(self, enviroment, verbose = False):
        self.env = enviroment
        self.verbose = verbose

    def game(self):
        done = False
        if self.verbose:
            self.env.render()
            print()
        while not done:
            movement = random.randint(0,3)
            obs, reward, done, _ = self.env.step(movement)
            if self.verbose:
                self.env.render()
                print("You earned ", reward, ", total score: ", self.env.score)
        if self.verbose: print('\nYou lost, final score: ', self.env.score)
