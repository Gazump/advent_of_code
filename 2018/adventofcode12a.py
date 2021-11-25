# NMB
# AoC 2018
# Problem 12a

lines = open('puzzle_input_12.txt','r').read().splitlines()

rules = {}

for i in range(2,len(lines)):
    tokens = lines[i].split(' ')
    pattern = tokens[0]
    output = tokens[2]
    rules[pattern] = output
    
state = lines[0].split(' ')[2]
offset = 0

for i in range(20):
    new_gen = ''
    temp = '....'+state+'....'
    offset += 2
    for c in range(len(temp)-4):
        if temp[c:c+5] in rules:
            new_gen += rules[temp[c:c+5]]
        else:
            new_gen += '.'            
    state = new_gen  
    # strip leading and trailing '.'
    if state[:4] == '....':
        state = state[4:]
        offset -= 4
    if state[-4:] == '....':
        state = state[:-4]

score = 0
for i,c in enumerate(state):
    if c == '#':
        score += (i-offset)
print(score)
