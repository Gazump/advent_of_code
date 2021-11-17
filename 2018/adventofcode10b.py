# NMB
# AoC 2018
# Problem 10a

import re

lines = open('puzzle_input_10.txt','r').read().splitlines()
coords, origin_coords, vels, high, low = [], [], [], 0, 999999

for line in lines:
    tokens = re.split('<|,|>', line)
    high = max(high,int(tokens[1]),int(tokens[2]))
    low = min(low,int(tokens[1]),int(tokens[2]))
    origin_coords.append((int(tokens[1]),int(tokens[2])))
    coords.append((int(tokens[1]),int(tokens[2])))
    vels.append((int(tokens[4]),int(tokens[5])))

min_count = 0
min_hyp = 99999999
increase = 0

secs = 1
while increase < 2:
    top_left = (-999999, -999999)
    bot_right = (999999, 999999)
    for i,c in enumerate(coords):
        coords[i] = (c[0]+vels[i][0],c[1]+vels[i][1])
        temp = (c[0]+vels[i][0],c[1]+vels[i][1])        
        if coords[i] > top_left:
            top_left = temp            
        elif coords[i] < bot_right:
            bot_right = temp
    hyp = abs(top_left[0]-bot_right[0]) + abs(top_left[1]-bot_right[1])
    if hyp < min_hyp:
        min_hyp = hyp
        min_count = secs
        increase = 0
    else:
        increase += 1
    secs += 1
    
print(min_count)
