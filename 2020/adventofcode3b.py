# Boshoff
# advent of code 3b

grid = open('puzzle_input_3.txt','r').read().splitlines()

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
counts, w, h = 1, len(grid[0])-1, len(grid)-1
for slope in slopes:
    x,y,count = 0,0,0
    while y < h:
        x += slope[0]
        y += slope[1]
        x -= (w+1) * (x > w)
        count += (grid[y][x] == '#')
    counts *= count
print(counts)
