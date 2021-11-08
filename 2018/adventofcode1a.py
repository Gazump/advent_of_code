# NMB
# AoC 2018
# Problem 1a

lines = open('puzzle_input_1.txt','r').read().splitlines()
num = 0

for line in lines:
    if line[0] == '+':
        num += int(line[1:])
    else:
        num -= int(line[1:])

print(num)
