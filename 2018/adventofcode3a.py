# NMB
# AoC 2018
# Problem 3a
import numpy as np

lines = open('puzzle_input_3.txt','r').read().splitlines()
grid = [[0]*1000 for i in range(1000)]
for line in lines:
    tokens = line.split(' ')
    start, size = tokens[2].split(','), tokens[3].split('x')
    left, top, width, height = int(start[0]), int(start[1][:-1]), int(size[0]), int(size[1])
    for x in range(left,left+width):
        for y in range(top, top+height):
            grid[y][x] += 1
array = np.array(grid)
print((array>1).sum())
    


    
    

                

                
    







        

    
        
    

