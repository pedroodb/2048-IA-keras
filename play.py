from enviroment import Enviroment
from agents import RandomAgent, InteractiveAgent

op = input("Press 1 to start a game, press 2 for a random play\n")
if op == '1':
    a = InteractiveAgent(Enviroment())
else:
    a = RandomAgent(Enviroment(), True)
a.game()