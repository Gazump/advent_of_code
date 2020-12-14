# Boshoff
# advent of code 2020 - 10a

numbers = sorted([int(x) for x in open('puzzle_input_10.txt','r').read().splitlines()])
numbers.append(max(numbers)+3)

one, three = 0, 0
current = 0
last = 0

for num in numbers:   
    if num - current == 1:
        one += 1 
    elif num - current == 3:
        three += 1
    current = num
print(one,three, one*three)
    


            
    
    
    

  
