# NMB
# Advent of Code 2021
# Problem 10b

lines = open('input_10.txt','r').read().splitlines()

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)

flashes = 0
step = 0
while flashes < 100:
    flashes = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1    
    flash = True
    while flash:
        flash = False
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 9:
                    flash = True
                    flashes += 1
                    #increase all adjacents
                    for x in range(max(0,c-1),min(len(grid[0]),c+2)):
                        for y in range(max(0,r-1),min(len(grid),r+2)):
                            if grid[y][x] != -1:
                                grid[y][x] += 1
                    grid[r][c] = -1

    # clear -1's
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == -1:
                grid[r][c] = 0
    step += 1

print(step)                   