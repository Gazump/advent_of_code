# NMB
# Advent of Code 2021
# Problem 07a

nums = sorted([int(x) for x in open('input_7.txt','r').read().split(',')])

small_i = -1
smallest = 9999999999999

for i in range(0,max(nums)+1):
    total = 0
    for n in nums:        
        total += abs(i - n)
    if total < smallest:
        smallest = total
        small_i = i
print(smallest)


    



        
        



    
        
                        
                        
                        
                        


            
    
        
                        

