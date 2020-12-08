# Boshoff
# advent of code 2020 - 8a

lines = open('puzzle_input_8.txt','r').read().splitlines()

acc = 0
op_pos = 0
executed = [0]*len(lines)

while not executed[op_pos]:    
    args = lines[op_pos].split(' ')

    if args[0] == 'acc':
        acc += int(args[1])
        executed[op_pos] = True
        op_pos += 1
    elif args[0] == 'nop':
        executed[op_pos] = True
        op_pos += 1
    elif args[0] == 'jmp':
        executed[op_pos] = True
        op_pos += int(args[1])
        
print(acc)
    

  
