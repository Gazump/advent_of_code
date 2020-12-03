# Boshoff
# advent of code 2019 - 1b

def calculate_fuel(n):    
    fuel = int(n) // 3 - 2    
    if fuel > 0:
        return fuel + calculate_fuel(fuel)
    else:
        return 0

# main
numbers = open('puzzle_input_1.txt','r').read().splitlines()
total_fuel = 0
for num in numbers:
    total_fuel += calculate_fuel(num)
print(total_fuel)
    
    


    
    








