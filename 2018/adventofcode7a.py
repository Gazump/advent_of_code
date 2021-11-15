# NMB
# AoC 2018
# Problem 7a

lines = open('puzzle_input_7.txt','r').read().splitlines()
nodes = {}

for line in lines:
    tokens = line.split(" ")
    parent, child = tokens[1], tokens[7]    

    if child not in nodes:
        nodes[child] = [parent]
    else:
        nodes[child].append(parent)
        nodes[child] = sorted(nodes[child],reverse=True)

    if parent not in nodes:
        nodes[parent] = []

c = ord('A')
completed = []

while len(completed) < len(nodes):
    if chr(c) in nodes and chr(c) not in completed:
        ready = True
        if len(nodes[chr(c)]) > 0:        
            for dependent in nodes[chr(c)]:
                if dependent not in completed:
                    ready = False
        if ready:
            completed.append(chr(c))
            c = ord('A')-1
    c += 1
    if c > ord('Z'):
        c = ord('A')
        
[print(x,end='') for x in completed]
