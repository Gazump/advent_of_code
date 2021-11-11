# NMB
# AoC 2018
# Problem 3a
import numpy as np

lines = open('puzzle_input_3.txt','r').read().splitlines()
grid = [[0]*1000 for i in range(1000)]
named_grid = [[0]*1000 for i in range(1000)]

for i,line in enumerate(lines):
    tokens = line.split(' ')
    start, size = tokens[2].split(','), tokens[3].split('x')
    left, top, width, height = int(start[0]), int(start[1][:-1]), int(size[0]), int(size[1])
    for x in range(left,left+width):
        for y in range(top, top+height):
            grid[y][x] += 1

# horrible brute force check... I should really fix this
for i,line in enumerate(lines):
    tokens = line.split(' ')
    start, size = tokens[2].split(','), tokens[3].split('x')
    left, top, width, height = int(start[0]), int(start[1][:-1]), int(size[0]), int(size[1])
    perfect = True
    for x in range(left,left+width):
        for y in range(top, top+height):
            if grid[y][x] != 1:
                perfect = False            
    if perfect:
        print(line)
                
