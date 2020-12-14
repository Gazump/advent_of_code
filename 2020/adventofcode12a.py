# Boshoff
# advent of code 2020 - 12a

lines = open('puzzle_input_12.txt','r').read().splitlines()

NORTH,EAST,SOUTH,WEST = 0, 1, 2, 3
dirs = [NORTH,EAST,SOUTH,WEST]
long, lat, face = 0, 0, 1
for line in lines:
    instr, num = line[0], int(line[1:])    
    if instr == 'N':
        long -= num
    elif instr == 'S':
        long += num
    elif instr == 'W':
        lat -= num
    elif instr == 'E':
        lat += num
    elif instr == 'L':        
        face = dirs[face-1*(num//90)]
    elif instr == 'R':                
        face = dirs[(face+1*(num//90))%4]        
    elif instr == 'F':
        if face == NORTH:
            long -= num
        elif face == SOUTH:
            long += num
        elif face == WEST:
            lat -= num
        elif face == EAST:
            lat += num
print(abs(long)+abs(lat))
