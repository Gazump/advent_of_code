# Boshoff
# advent of code 2020 - 12a

lines = open('puzzle_input_12.txt','r').read().splitlines()

NORTH,EAST,SOUTH,WEST = 0, 1, 2, 3
dirs = [NORTH,EAST,SOUTH,WEST]
way_long, way_lat = -1, 10
ship_long, ship_lat = 0, 0

for line in lines:
    instr, num = line[0], int(line[1:])    
    if instr == 'N':
        way_long -= num
    elif instr == 'S':
        way_long += num
    elif instr == 'W':
        way_lat -= num
    elif instr == 'E':
        way_lat += num
    elif instr == 'L':
        for i in range(num//90):
            way_lat, way_long = way_long, -way_lat       
    elif instr == 'R':
        for i in range(num//90):
            way_lat, way_long = -way_long, way_lat
    elif instr == 'F':
        ship_lat += way_lat*num
        ship_long += way_long*num
print(abs(ship_long)+abs(ship_lat))
