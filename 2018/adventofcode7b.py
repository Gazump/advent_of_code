# NMB
# AoC 2018
# Problem 7b

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
completed, working = [], []
workers = [['.',0] for i in range(5)]
steps = 0

while len(completed) < len(nodes):
    # assign work to workers
    for c in range(ord('A'),ord('Z')+1):
        if chr(c) in nodes and chr(c) not in completed and chr(c) not in working:
            ready = True
            if len(nodes[chr(c)]) > 0:        
                for dependent in nodes[chr(c)]:
                    if dependent not in completed:
                        ready = False            
            if ready:
                # add to worker
                for w in range(len(workers)):
                    if workers[w][1] == 0:                        
                        workers[w] = [chr(c),c-4] # + 60 - 64
                        working.append(chr(c))                        
                        break    
    # work
    for w in range(len(workers)):
        if workers[w][1] > 0:
            workers[w][1] -= 1
            if workers[w][1] == 0:
                completed.append(workers[w][0])
                working.remove(workers[w][0])
                workers[w] = ['.',0]
    steps += 1            

print(steps)
