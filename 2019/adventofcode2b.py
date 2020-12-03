# Boshoff
# advent of code 2019 - 2b

def gravity_search(numbers):
    for noun in range(100):
        for verb in range(100):
            memory = list(numbers)
            memory[1],memory[2] = noun, verb
            op_pos = 0
            while memory[op_pos] != 99:
                opcode = memory[op_pos]
                if opcode == 1:
                    memory[memory[op_pos+3]] = memory[memory[op_pos+1]] + memory[memory[op_pos+2]]
                elif opcode == 2:
                    memory[memory[op_pos+3]] = memory[memory[op_pos+1]] * memory[memory[op_pos+2]]
                op_pos += 4
            if memory[0] == 19690720:
                return 100 * noun + verb
            
# main
numbers = open('puzzle_input_2.txt','r').read().split(',')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(gravity_search(numbers))
        





