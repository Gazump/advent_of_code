# NMB
# Advent of Code 2021
# Problem 13a

lines = open('input_13.txt','r').read().splitlines()

grid, folds = [['.']*1310 for i in range(1310)], []

for line in lines:
    if line[:4] == 'fold':
        folds.append(line[line.index('=')-1:])
    elif line == '':
        pass
    else:
        tokens = line.split(',')
        grid[int(tokens[1])][int(tokens[0])] = '#'

fold = folds[0]
num = int(fold[2:])
if fold[0] == 'x':
    for i in range(len(grid)):
        grid[i][num] = '-'
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if c > num:
                grid[r][c] = '.'
            elif 2*num-c < len(grid) and grid[r][2*num-c] == '#':
                grid[r][c] = '#'
else:
    for i in range(len(grid[0])):
        grid[num][i] = '-'
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if r > num:
                grid[r][c] = '.'
            elif 2*num-r < len(grid[0]) and grid[2*num-r][c] == '#':
                grid[r][c] = '#'

print(sum([i.count('#') for i in grid]))
        


    
    


