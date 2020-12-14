# Boshoff
# advent of code 2020 - 11b
from copy import deepcopy

s_grid = open('puzzle_input_11.txt','r').read().splitlines()
grid = []

# listify a string
for row in s_grid:
    new_row = []
    for char in row:
        new_row.append(char)
    grid.append(new_row)       

done = False
ite = 0
while not done:
    ite += 1
    changed = False
    new_grid = deepcopy(grid)
    for y,row in enumerate(grid):        
        for x,seat in enumerate(row):            
            adj = 0
            xi, yi = -1,0
            while x + xi >= 0 and grid[y][x+xi] == '.':
                xi -= 1            
            if x + xi >= 0 and grid[y][x+xi] == '#':
                adj += 1
                
            xi, yi = 1,0
            while x + xi < len(row) and grid[y][x+xi] == '.':
                xi += 1
            if x + xi < len(row) and grid[y][x+xi] == '#':
                adj += 1

            xi, yi = 0,-1
            while y + yi >= 0 and grid[y+yi][x] == '.':
                yi -= 1            
            if y + yi >= 0 and grid[y+yi][x] == '#':
                adj += 1
                
            xi, yi = 0,1
            while y + yi < len(grid) and grid[y+yi][x] == '.':
                yi += 1            
            if y + yi < len(grid) and grid[y+yi][x] == '#':
                adj += 1

            xi, yi = -1,-1
            while x + xi >= 0 and y + yi >= 0 and grid[y+yi][x+xi] == '.':
                xi -= 1
                yi -= 1
            if x + xi >= 0 and y + yi >= 0 and grid[y+yi][x+xi] == '#':
                adj += 1

            xi, yi = -1,1
            while x + xi >= 0 and y + yi < len(grid) and grid[y+yi][x+xi] == '.':
                xi -= 1
                yi += 1
            if x + xi >= 0 and y + yi < len(grid) and grid[y+yi][x+xi] == '#':
                adj += 1

            xi, yi = 1,1
            while x + xi < len(row) and y + yi < len(grid) and grid[y+yi][x+xi] == '.':
                xi += 1
                yi += 1
            if x + xi < len(row) and y + yi < len(grid) and grid[y+yi][x+xi] == '#':
                adj += 1

            xi, yi = 1,-1
            while x + xi < len(row) and y + yi >= 0 and grid[y+yi][x+xi] == '.':
                xi += 1
                yi -= 1                
            if x + xi < len(row) and y + yi >= 0 and grid[y+yi][x+xi] == '#':
                adj += 1

            if seat == 'L' and adj == 0:                
                new_grid[y][x] = '#'
                changed = True
            elif seat == '#' and adj >= 5:
                new_grid[y][x] = 'L'
                changed = True

    if ite % 100 == 0:
        print(ite)
    grid = deepcopy(new_grid)
    done = not changed

c = 0
for row in grid:
    for seat in row:
        c += (seat == '#')

print(c)
