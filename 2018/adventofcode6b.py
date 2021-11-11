# NMB
# AoC 2018
# Problem 6b

lines = open('puzzle_input_6.txt','r').read().splitlines()
size = 400
grid = [['.']*size for i in range(size)]
label = 65
coords = []
min_x, min_y, max_x, max_y = size, size, 0, 0

for line in lines:
    tokens = line.split(' ')
    x, y = int(tokens[0][:-1]), int(tokens[1])
    min_x, min_y = min(x,min_x), min(y, min_y)
    max_x, max_y = max(x,max_x), max(y, max_y)
    if label > 90:
        grid[y][x] = chr(label-26)*2
    else:
        grid[y][x] = chr(label)
    coords.append([grid[y][x],x,y])
    label += 1
for y in range(size): 
    for x in range(size):
        total = 0
        for c in coords:
            total += abs(x-c[1]) + abs(y-c[2])
            if total >= 10000:
                break
        if total < 10000:
            grid[x][y] = '#'

print(sum(row.count('#') for row in grid))

    
    



    
    
    



 
                
