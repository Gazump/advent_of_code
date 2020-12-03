# Boshoff
# advent of code 2019 - 2a

numbers = open('puzzle_input_2.txt','r').read().split(',')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[1],numbers[2] = 12, 2

op_pos = 0
while numbers[op_pos] != 99:
    opcode = numbers[op_pos]
    if opcode == 1:
        numbers[numbers[op_pos+3]] = numbers[numbers[op_pos+1]] + numbers[numbers[op_pos+2]]
    elif opcode == 2:
        numbers[numbers[op_pos+3]] = numbers[numbers[op_pos+1]] * numbers[numbers[op_pos+2]]
    op_pos += 4
print(numbers[0])    
        





