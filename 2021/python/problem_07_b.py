# NMB
# Advent of Code 2021
# Problem 07b

nums = sorted([int(x) for x in open('input_07.txt','r').read().split(',')])

small_i = -1
smallest = 9999999999999

for i in range(0,max(nums)):
    total = 0
    for n in nums:
        #for j in range(0,abs(n-i)+1):
        #    total += j
        m = abs(n - i)+1
        total += m*(m-1)/2
    if total < smallest:
        smallest = total
        small_i = i
    #print(i, total)
print(small_i, smallest)


    



        
        



    
        
                        
                        
                        
                        


            
    
        
                        

