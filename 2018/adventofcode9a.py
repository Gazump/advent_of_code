# NMB
# AoC 2018
# Problem 9a

lines = open('puzzle_input_9.txt','r').read().split(' ')

players, last = int(lines[0]), int(lines[6])
circle, turn, scores, current = [0,2,1], 2, [0]*players, 1

for i in range(3,last+1):
    if i % 23 == 0:
        scores[turn] += i
        current -= 7
        if current < 0:
            current += len(circle)
        scores[turn] += circle.pop(current)
    else:
        current += 2
        if current == len(circle):
            circle.append(current)
        elif current > len(circle):
            current = current % len(circle)
            circle.insert(current, i)
        else:
            circle.insert(current, i)     
        turn = (turn + 1) % players

print(max(scores))
    
    


    

    
        

    

    

    
    




