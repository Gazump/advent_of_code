# NMB
# Advent of Code 2021
# Problem 01b

lines = open('input_1.txt','r').read().splitlines()
c, prev = 0, 999999

for i in range(2,len(lines)):
    total = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
    if total > prev:
        c += 1
    prev = total

print(c)
    
