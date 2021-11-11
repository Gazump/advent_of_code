# NMB
# AoC 2018
# Problem 6a

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
        closest = ''
        distance = size*2 + 1
        for i in range(len(coords)):            
            t_dist = abs(x-coords[i][1]) + abs(y-coords[i][2])
            if t_dist < distance:
                closest = coords[i][0]
                distance = t_dist
            elif t_dist == distance:
                closest = '.'
        if distance != 0:
            grid[y][x] = closest.lower()

biggest = ''
biggest_area = 0
for c in coords:
    label = c[0].lower()
    if (label not in grid[0] and
        label not in grid[size-1] and
        label not in [row[0] for row in grid] and
        label not in [row[size-1] for row in grid]):        
        count = sum(row.count(label) for row in grid)
        if count > biggest_area:
            biggest_area = count
            biggest = label       

print(biggest, biggest_area+1)
