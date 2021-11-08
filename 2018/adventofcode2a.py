# NMB
# AoC 2018
# Problem 2a
lines = open('puzzle_input_2.txt','r').read().splitlines()
twos, threes = 0, 0
for line in lines:
    freq = {}
    for c in line:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    twos += (2 in freq.values())        
    threes += (3 in freq.values())
print(twos*threes)
        

    
        
    

