# Boshoff
# advent of code 2020 - 5a

print(max([int(num[:7].replace('F','0').replace('B','1'),2)*8+int(num[7:].replace('L','0').replace('R','1'),2) for num in open('puzzle_input_5.txt','r').read().splitlines()]))
