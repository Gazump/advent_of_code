# NMB
# Advent of Code 2021
# Problem 02a

lines = open('input_2.txt','r').read().splitlines()
h, d = 0, 0
for line in lines:
    tokens = line.split(" ")
    if tokens[0] == "forward":
        h += int(tokens[1])
    elif tokens[0] == "down":
        d += int(tokens[1])
    else:
        d -= int(tokens[1])
print(d*h)
        
