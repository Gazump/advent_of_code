# Boshoff
# advent of code 2020 - 8b

# Hacky solution. TODO swap smartly instead of duplicating
# entire list each time

f_lines = open('puzzle_input_8.txt','r').read().splitlines()
r_c = 0
success = False
while not success:
    o_lines = f_lines
    lines = []
    r_i = 0
    swapped = False
    # replace stuff
    for line in o_lines:
        args = line.split(' ')
        if args[0] == 'nop' or args[0] == 'jmp':
            if r_i == r_c and not swapped:
                # swap
                if args[0] == 'nop':
                    args[0] = 'jmp'
                else:
                    args[0] = 'nop'
                swapped = True
                r_c += 1
            r_i += 1                
        lines.append(args[0]+' '+args[1])
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
        if op_pos >= len(lines):
            print(acc)
            success = True
            break
