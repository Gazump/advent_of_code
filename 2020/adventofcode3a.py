# Boshoff
# advent of code 3a

grid = open('puzzle_input_3.txt','r').read().splitlines()

slope, w, h = (3,1), len(grid[0])-1, len(grid)-1
x,y,count = 0,0,0
while y < h:
    x += slope[0]
    y += slope[1]
    x -= (w+1) * (x > w)        # naughty! use if x>w then x-=w+1        
    count += (grid[y][x] == '#')# again, if grid[y][x]== '#' then count += 1        
print(count)
