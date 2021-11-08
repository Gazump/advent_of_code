# AoC 2018
# Problem 1b
lines = open('puzzle_input_1.txt','r').read().splitlines()
num, c , visited, = 0, 0, {}

while not num in visited:
    visited[num] = 1
    num += int(lines[c%len(lines)])    
    c += 1
    
print(num)
        
    

