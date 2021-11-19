# NMB
# AoC 2018
# Problem 11a

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
        
largest = 0
largest_c = (-1,-1)
for y in range(300-3):
    for x in range(300-3):
        size = 0
        for c in range(x,x+3):
            size += sum(grid[r][c] for r in range(y,y+3))
        if size > largest:
            largest = size
            largest_c = (x,y)

print(largest_c[0]+1,',',largest_c[1]+1,sep='')
