# NMB
# AoC 2018
# Problem 9b

import collections

lines = open('puzzle_input_9.txt','r').read().split(' ')

players, last = int(lines[0]), int(lines[6])*100
circle, turn, scores = collections.deque([0,2,1]), 2, [0]*players

for i in range(3,last+1):
    if i % 23 == 0:
        scores[turn] += i
        circle.rotate(7)       
        scores[turn] += circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(i)
        turn = (turn + 1) % players   
print(max(scores))
    
    


    

    
        

    

    

    
    




