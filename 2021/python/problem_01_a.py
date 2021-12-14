# NMB
# Advent of Code 2021
# Problem 01a

lines = open('input_01.txt','r').read().splitlines()
c, prev = 0, 999999
for line in lines:
    if int(line) > prev:
        c += 1
    prev = int(line)
print(c)
    
