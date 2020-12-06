# Boshoff
# advent of code 2019 - 5b

numbers = open('puzzle_input_5.txt','r').read().split(',')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

op_pos = 0
while numbers[op_pos] != 99:
    opcode = numbers[op_pos]
    A,B,C = 0,0,0
    if opcode > 8:
        # we have a parameter mode
        #fill up to 5 digits
        ABCDE = (5-len(str(opcode)))*'0' + str(opcode)
        opcode = int(ABCDE[3:])
        A,B,C = int(ABCDE[0]),int(ABCDE[1]),int(ABCDE[2])
    
    if opcode == 1:
        first,second = 0,0
        if C == 0:
            first = numbers[numbers[op_pos+1]]
        else:
            first = numbers[op_pos+1]
        if B == 0:
            second = numbers[numbers[op_pos+2]]
        else:
            second = numbers[op_pos+2]         
                 
        numbers[numbers[op_pos+3]] = first + second
        
        op_pos += 4
    elif opcode == 2:

        first,second = 0,0
        if C == 0:
            first = numbers[numbers[op_pos+1]]
        else:
            first = numbers[op_pos+1]
        if B == 0:
            second = numbers[numbers[op_pos+2]]
        else:
            second = numbers[op_pos+2]
            
        numbers[numbers[op_pos+3]] = first * second
        
        op_pos += 4
    elif opcode == 3:
        given = int(input('Enter the input: '))        
        numbers[numbers[op_pos+1]] = given
        
        op_pos += 2
    elif opcode == 4:
        if C == 0:            
            print("OUTPUT:",numbers[numbers[op_pos+1]])
        else:
            print("OUTPUT:",numbers[op_pos+1])
        op_pos += 2
    elif opcode == 5:
        flag = False
        if C == 0:
            if numbers[numbers[op_pos+1]] != 0:
                flag = True
        else:
            if numbers[op_pos+1] != 0:
                flag = True
        if flag:
            if B == 0:
                op_pos = numbers[numbers[op_pos+2]]
            else:
                op_pos = numbers[op_pos+2]
        else:
            op_pos += 3
    elif opcode == 6:
        flag = False
        if C == 0:
            if numbers[numbers[op_pos+1]] == 0:
                flag = True
        else:
            if numbers[op_pos+1] == 0:
                flag = True
        if flag:
            if B == 0:
                op_pos = numbers[numbers[op_pos+2]]
            else:
                op_pos = numbers[op_pos+2]
        else:
            op_pos += 3
    elif opcode == 7:
        first,second = 0,0
        if C == 0:
            first = numbers[numbers[op_pos+1]]
        else:
            first = numbers[op_pos+1]
        if B == 0:
            second = numbers[numbers[op_pos+2]]
        else:
            second = numbers[op_pos+2]

        if first < second:    
            numbers[numbers[op_pos+3]] = 1
        else:
            numbers[numbers[op_pos+3]] = 0
            
        op_pos += 4
    elif opcode == 8:
        first,second = 0,0
        if C == 0:
            first = numbers[numbers[op_pos+1]]
        else:
            first = numbers[op_pos+1]
        if B == 0:
            second = numbers[numbers[op_pos+2]]
        else:
            second = numbers[op_pos+2]

        if first == second:    
            numbers[numbers[op_pos+3]] = 1
        else:
            numbers[numbers[op_pos+3]] = 0
        
        op_pos += 4
    else:
        print("ERROR!")
