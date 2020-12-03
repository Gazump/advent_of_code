# Boshoff
# advent of code 2020 - 1b

file = open('puzzle_input_1.txt','r')

numbers = []
for line in file:
    numbers.append(int(line))

def find_product():
    for n in numbers:
        if len(str(n)) == 3:
            for m in numbers:
                if len(str(n)) == 3:
                    for l in numbers:
                        if l + m + n  == 2020:
                            return l*m*n

print(find_product())





