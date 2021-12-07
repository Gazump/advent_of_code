# NMB
# Advent of Code 2021
# Problem 05b

import time
import numpy as np
import matplotlib.pyplot as plt

lines = open('~/../../input_5.txt','r').read().splitlines()
grid = [[0]*1000 for i in range(1000)]

fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(np.array(grid), vmin=0, vmax=5, cmap='hot')
plt.show(block=False)
plt.pause(1)

delay = 0.01

for line in lines:
    updated = False
    tokens = line.split('->')
    c1 = [int(c) for c in tokens[0].split(',')]
    c2 = [int(c) for c in tokens[1].split(',')]
    if c1[0] == c2[0] or c1[1] == c2[1]:
        for x in range( min(c1[0],c2[0]), max(c1[0],c2[0])+1):
            for y in range( min(c1[1],c2[1]), max(c1[1],c2[1])+1):
                grid[y][x] += 1
                updated = True
    else:
        if c1[0] > c2[0]:
            diff = -1
        else:
            diff = 1
        for c in range( c1[0], c2[0]+diff, diff ):
            if c1[1] > c2[1]:
                y = c1[1] - (abs(c1[0] - c))
            else:
                y = c1[1] + (abs(c1[0] - c))
            grid[y][c] += 1
            updated = True
    if updated:
        plt.clf()
        plt.imshow(np.array(grid), vmin=0, vmax=5, cmap='hot')    
        plt.pause(delay)
