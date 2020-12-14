# Boshoff
# advent of code 2020 - 10b

from collections import Counter

numbers = sorted([int(x) for x in open('puzzle_input_10.txt','r').read().splitlines()])
numbers.append(numbers[-1]+3)

arrangements = Counter()
arrangements[0] = 1

for num in numbers:    
    arrangements[num] = arrangements[num-1] + arrangements[num-2] + arrangements[num-3]
    
print(arrangements[numbers[-1]])
