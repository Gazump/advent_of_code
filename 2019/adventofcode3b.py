# Boshoff
# advent of code 2019 - 3b

lines = open('puzzle_input_3.txt','r').read().splitlines()

# calculate dimensions
lowx,highx,lowy,highy = 0,0,0,0
x,y = 0,0
for line in lines:
    x,y = 0,0
    moves = line.split(',')    
    for move in moves:
        if move[0] == 'R':
            x += int(move[1:])
            if x > highx:
                highx = x            
        elif move[0] == 'L':
            x -= int(move[1:])
            if x < lowx:
                lowx = x
        elif move[0] == 'D':
            y += int(move[1:])
            if y > highy:
                highy = y
        elif move[0] == 'U':
            y -= int(move[1:])
            if y < lowy:
                lowy = y

grid = []

print('Creating grid...')

# set up blank grid
for y in range(highy-lowy):
    row = list('.'*(highx-lowx))    
    grid.append(row)

print('Done!')

# central port
x = 0
y = 0
grid[y][x] = 'O'

crossings = []

def update_grid(player,x,y):
    if grid[y][x] == '.':
        grid[y][x] = str(player)
    elif (grid[y][x] == str(player) or
          grid[y][x] == 'O' or
          grid[y][x] == 'X'):
        pass
    else:   #other player
        grid[y][x] = 'X'
        crossings.append((x,y))

# for each path
player = 0
for line in lines:
    x,y=0,0
    player += 1
    moves = line.split(',')
    for move in moves:
        if move[0] == 'R':
            for i in range(0,int(move[1:])):
                x += 1
                update_grid(player,x,y)            
        elif move[0] == 'L':
            for i in range(0,int(move[1:])):
                x -= 1
                update_grid(player,x,y)
        elif move[0] == 'D':
            for i in range(0,int(move[1:])):
                y += 1
                update_grid(player,x,y)
        elif move[0] == 'U':
            for i in range(0,int(move[1:])):
                y -= 1
                update_grid(player,x,y)

crossing_steps = [0]*len(crossings)
crossing_flags = [False]*len(crossings)
step = 0
for line in lines:
    x,y = 0,0
    step = 0
    moves = line.split(',')
    for i in range(len(crossing_flags)):
        crossing_flags[i] = False
    for move in moves:        
        if move[0] == 'R':
            for i in range(0,int(move[1:])):
                step += 1
                x += 1
                if (x,y) in crossings and not crossing_flags[crossings.index((x,y))]:            
                    crossing_steps[crossings.index((x,y))] += step
                    crossing_flags[crossings.index((x,y))] = True            
        elif move[0] == 'L':
            for i in range(0,int(move[1:])):
                step += 1
                x -= 1
                if (x,y) in crossings and not crossing_flags[crossings.index((x,y))]:            
                    crossing_steps[crossings.index((x,y))] += step
                    crossing_flags[crossings.index((x,y))] = True 
        elif move[0] == 'D':
            for i in range(0,int(move[1:])):
                step += 1
                y += 1
                if (x,y) in crossings and not crossing_flags[crossings.index((x,y))]:            
                    crossing_steps[crossings.index((x,y))] += step
                    crossing_flags[crossings.index((x,y))] = True 
        elif move[0] == 'U':
            for i in range(0,int(move[1:])):
                step += 1
                y -= 1
                if (x,y) in crossings and not crossing_flags[crossings.index((x,y))]:            
                    crossing_steps[crossings.index((x,y))] += step
                    crossing_flags[crossings.index((x,y))] = True      

print(min(crossing_steps))
                
                           









