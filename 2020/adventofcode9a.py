# Boshoff
# advent of code 2020 - 9a

numbers = [int(x) for x in open('puzzle_input_9.txt','r').read().splitlines()]

def brute_force(i,numbers):    
    for j in range(i-25,i-1):
        for k in range(j+1,i):            
            if numbers[j] + numbers[k] == numbers[i]:                
                return True
    return False


# MAIN
for i in range(25,len(numbers)):
    if not brute_force(i,numbers):
        print(numbers[i])
        break
            
    
    
    

  
