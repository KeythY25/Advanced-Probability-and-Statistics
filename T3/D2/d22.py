import numpy as np
import random
import matplotlib.pyplot as plt

def coinFlip(nflips):
    flips = np.zeros(nflips)
    for flip in range(nflips):
        flips[flip] = random.choice([0,1])
    return flips

t1 = coinFlip(100)
t2 = coinFlip(100)
t3 = coinFlip(100)

print(np.sum(t1))
print(np.sum(t2))
print(np.sum(t3))

