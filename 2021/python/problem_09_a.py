# NMB
# Advent of Code 2021
# Problem 09a

lines = open('input_09.txt','r').read().splitlines()

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)       

lows = []
for y,row in enumerate(grid):
    for x,n in enumerate(row):
        if x > 0 and x < len(row)-1 and y > 0 and y < len(grid)-1:
            if n < grid[y-1][x] and n < grid[y+1][x] and n < grid[y][x-1] and n < grid[y][x+1]:
                lows.append(n)                
        elif x == 0 and y == 0:
            if n < grid[y+1][x] and n < grid[y][x+1]:
                lows.append(n)
        elif x == len(row)-1 and y == len(grid)-1:
            if n < grid[y-1][x] and n < grid[y][x-1]:
                low.append(n)
        elif x == len(row)-1 and y == 0:
            if n < grid[y+1][x] and n < grid[y][x-1]:
                lows.append(n)
        elif x == 0 and y == len(grid)-1:
            if n < grid[y-1][x] and n < grid[y][x+1]:
                low.append(n)
        elif x == 0:
            if n < grid[y-1][x] and n < grid[y+1][x] and n < grid[y][x+1]:
                lows.append(n)
        elif y == 0:
            if n < grid[y][x-1] and n < grid[y+1][x] and n < grid[y][x+1]:
                lows.append(n)
        elif x == len(row)-1:
            if n < grid[y][x-1] and n < grid[y+1][x] and n < grid[y-1][x]:
                lows.append(n)
        elif y == len(grid)-1:
            if n < grid[y][x-1] and n < grid[y][x+1] and n < grid[y-1][x]:
                lows.append(n)

print(sum(lows)+len(lows))
        
            
        
    

    

    







    



        
        



    
        
                        
                        
                        
                        


            
    
        
                        

