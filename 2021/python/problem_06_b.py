# NMB
# Advent of Code 2021
# Problem 06b

from collections import Counter

nums = [int(x) for x in open('input_6.txt','r').read().split(',')]

ages = Counter()
for n in nums:
    ages[n] += 1

for day in range(256):
    new = 0
    now = sorted(ages.keys(),reverse=False)
    for key in now:        
        if key == 0:      
            new += ages[0]
            ages[0] = 0
        else:   
            ages[key-1] += ages[key]
            ages[key] = 0
    ages[6] += new 
    ages[8] += new
    
print(sum(ages.values()))
        



        
        



    
        
                        
                        
                        
                        


            
    
        
                        

