# NMB
# Advent of Code 2021
# Problem 02b

lines = open('input_02.txt','r').read().splitlines()
h, d, a = 0, 0, 0
for line in lines:
    tokens = line.split(" ")
    if tokens[0] == "forward":
        h += int(tokens[1])
        d += a*int(tokens[1])
    elif tokens[0] == "down":
        a += int(tokens[1])
    else:
        a -= int(tokens[1])
print(d*h)
