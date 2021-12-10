# NMB
# Advent of Code 2021
# Problem 09b

lines = open('input_9.txt','r').read().splitlines()
grid = []
basins = []
for line in lines:
    row = []
    b_row = []
    for c in line:
        row.append(int(c))
        b_row.append('z')
    grid.append(row)
    basins.append(b_row)

new_basin = 65
for y,row in enumerate(grid):
    for x,n in enumerate(row):
        if n != 9:
            if x > 0 and grid[y][x-1] < 9 and basins[y][x-1] != 'z':
                basins[y][x] = basins[y][x-1]
            elif x < len(row)-1 and grid[y][x+1] < 9 and basins[y][x+1] != 'z':
                basins[y][x] = basins[y][x+1]
            elif y > 0 and grid[y-1][x] != 9 and basins[y-1][x] != 'z':
                basins[y][x] = basins[y-1][x]
            elif y < len(grid)-1 and grid[y+1][x] < 9 and basins[y+1][x] != 'z':
                basins[y][x] = basins[y+1][x]
            else:
                basins[y][x] = chr(new_basin)
                new_basin += 1

change = True
while change:
    change = False
    for y in range(len(grid)):
        for x in range(len(grid[0])-1):
            if basins[y][x] != basins[y][x+1] and basins[y][x] != 'z' and basins[y][x+1] != 'z':
                for r in range(len(basins)):
                    for c in range(len(basins[0])):
                        if basins[r][c] == basins[y][x+1]:
                            basins[r][c] = basins[y][x]
                change = True

    for x in range(len(grid[0])):
        for y in range(len(grid)-1):
            if basins[y][x] != basins[y+1][x] and basins[y][x] != 'z' and basins[y+1][x] != 'z':

                for r in range(len(basins)):
                    for c in range(len(basins[0])):
                        if basins[r][c] == basins[y+1][x]:
                            basins[r][c] = basins[y][x]
                change = True

counts = {}

for row in basins:
    for ch in row:
        if ch not in counts and ch != 'z':
            counts[ch] = 1
        elif ch != 'z':
            counts[ch] += 1
best = sorted(counts, key=counts.get, reverse=True)[:3]

print(counts[best[0]]*counts[best[1]]*counts[best[2]])
