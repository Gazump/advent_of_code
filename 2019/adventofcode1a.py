# Boshoff
# advent of code 2019 - 1a

numbers = open('puzzle_input_1.txt','r').read().splitlines()
fuel = 0
for num in numbers:
    fuel += int(num) // 3 - 2
print(fuel)






