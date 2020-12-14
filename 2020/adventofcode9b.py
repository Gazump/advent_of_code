# Boshoff
# advent of code 2020 - 9b

numbers = [int(x) for x in open('puzzle_input_9.txt','r').read().splitlines()]

def bf_check_valid(i,numbers):    
    for j in range(i-25,i-1):
        for k in range(j+1,i):            
            if numbers[j] + numbers[k] == numbers[i]:                
                return True
    return False

def bf_find_sum(numbers):
    for i in range(len(numbers)):
        add = numbers[i]
        for j in range(i+1,len(numbers)):
            add += numbers[j]
            if add == invalid:
                return min(numbers[i:j+1])+max(numbers[i:j+1])


# MAIN
invalid = 0
for i in range(25,len(numbers)):
    if not bf_check_valid(i,numbers):
        invalid = numbers[i]
        break

print(invalid)

print(bf_find_sum(numbers))
            
    
    
    

  
