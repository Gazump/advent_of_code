# NMB
# Advent of Code 2021
# Problem 06a

nums = [int(x) for x in open('input_6.txt','r').read().split(',')]

for day in range(80):
    new = 0
    for i in range(len(nums)):
        nums[i] -= 1
        if nums[i] == -1:
            new += 1
            nums[i] = 6
    for i in range(new):
        nums.append(8)

print(len(nums))
        



        
        



    
        
                        
                        
                        
                        


            
    
        
                        

