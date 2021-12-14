# NMB
# Advent of Code 2021
# Problem 05b

lines = open('input_05.txt','r').read().splitlines()
grid = [[0]*1000 for i in range(1000)]

for line in lines:
    tokens = line.split('->')
    c1 = [int(c) for c in tokens[0].split(',')]
    c2 = [int(c) for c in tokens[1].split(',')]
    if c1[0] == c2[0] or c1[1] == c2[1]:
        for x in range( min(c1[0],c2[0]), max(c1[0],c2[0])+1):
            for y in range( min(c1[1],c2[1]), max(c1[1],c2[1])+1):
                grid[y][x] += 1
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
danger = 0
for row in grid:
    for c in row:
        if c >= 2:
            danger += 1
print(danger)
        
        



    
        
                        
                        
                        
                        


            
    
        
                        

