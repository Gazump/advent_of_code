# NMB
# AoC 2018
# Problem 11a

# VERY SLOW... needs optimisation...

import numpy as np

lines = open('puzzle_input_11.txt','r').read().splitlines()

serial = int(lines[0])

grid = [[0]*300 for i in range(300)]

for y in range(300):
    for x in range(300):
        rack_id = (x+1)+10
        power_level = rack_id * (y+1)        
        power_level += serial
        power_level *= rack_id
        power_level = int(str(power_level)[-3]) - 5
        grid[y][x] = power_level

array = np.asarray(grid)

largest = 0
largest_c = (-1,-1)
largest_s = 0
for s in range(1,300):    
    for y in range(300-s):
        for x in range(300-s):
            snap = array[y:y+s,x:x+s]
            size = np.cumsum(snap)[-1]
            if size > largest:
                largest = size
                largest_s = s
                largest_c = (x,y)

print(largest_c[0]+1,',',largest_c[1]+1,',',largest_s,sep='')
