# NMB
# Advent of Code 2021
# Problem 03a

lines = open('input_3.txt','r').read().splitlines()
g, e = '',''    
for i in range(len(lines[0])):
    c0, c1 = 0, 0
    for line in lines:
        if line[i] == '0':
            c0 += 1
        else:
            c1 += 1
    if c0 > c1:
        g += '0'
        e += '1'
    else:
        g += '1'
        e += '0'        
print(int(g,2)*int(e,2))
        
