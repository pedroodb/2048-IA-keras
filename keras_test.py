import numpy as np
import random
from enviroment import Enviroment, LOG_NORM

def gather_data(env):
    min_score = 1500
    trainingX, trainingY = [], []
    scores = []
    for i in range(10000):
        observation = env.reset()
        score = 0
        training_sampleX, training_sampleY = [], []
        done = False
        while not done:
            action = random.randint(0,3)
            one_hot_action = np.zeros(4)
            one_hot_action[action] = 1
            training_sampleX.append(observation)
            training_sampleY.append(one_hot_action)
            observation, reward, done, _ = env.step(action)
            score += reward
        print("Game ", i, " ended with score ", score)
        if score > min_score:
            scores.append(score)
            trainingX += training_sampleX
            trainingY += training_sampleY
    trainingX, trainingY = np.array(trainingX), np.array(trainingY)
    print("Average: {}".format(np.mean(scores)))
    print("Median: {}".format(np.median(scores)))
    return trainingX, trainingY

x, y = gather_data(Enviroment(LOG_NORM))
np.savetxt("data/initial_data", x, delimiter=",")
np.savetxt("data/initial_labels", y, delimiter=",")