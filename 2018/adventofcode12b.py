# NMB
# AoC 2018
# Problem 12b

lines = open('puzzle_input_12.txt','r').read().splitlines()

rules, saved = {}, {}

for i in range(2,len(lines)):
    tokens = lines[i].split(' ')
    pattern = tokens[0]
    output = tokens[2]
    rules[pattern] = output

state = lines[0].split(' ')[2]
offset, target = 0, -1

for i in range(50000000000):
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
    if target < 0:
        if state in saved:
            step = i - saved[state][0]
            target = i + (50000000000 - i - 1) % step            
            off_step = (offset - saved[state][1])//step         
            target_offset = (offset-(target-1)*off_step)+(50000000000-1)*off_step-1
        else:                        
            saved[state] = [i,offset]       
    if i == target:
        break

score = 0
for j,c in enumerate(state):
    if c == '#':
        score += (j-target_offset)          
print(score) 


    


        
        
    
    







