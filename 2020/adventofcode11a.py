# Boshoff
# advent of code 2020 - 11a
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
while not done:
    changed = False
    new_grid = deepcopy(grid)
    for y,row in enumerate(grid):        
        for x,seat in enumerate(row):            
            adj = 0
            if x > 0 and grid[y][x-1] == '#':
                adj += 1
            if x < len(row)-1 and grid[y][x+1] == '#':
                adj += 1
            if y > 0 and grid[y-1][x] == '#':
                adj += 1
            if y < len(grid)-1 and grid[y+1][x] == '#':
                adj += 1
            if x > 0 and y > 0 and grid[y-1][x-1] == '#':
                adj += 1
            if x > 0 and y < len(grid)-1 and grid[y+1][x-1] == '#':
                adj += 1
            if x < len(row)-1 and y < len(grid)-1 and grid[y+1][x+1] == '#':
                adj += 1
            if x < len(row)-1 and y > 0 and grid[y-1][x+1] == '#':
                adj += 1

            if seat == 'L' and adj == 0:                
                new_grid[y][x] = '#'
                changed = True
            elif seat == '#' and adj >= 4:
                new_grid[y][x] = 'L'
                changed = True
    
    grid = deepcopy(new_grid)
    done = not changed

c = 0
for row in grid:
    for seat in row:
        c += (seat == '#')

print(c)

            
            
            
                
                
    
    


            
    
    
    

  
