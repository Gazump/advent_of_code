# Boshoff
# advent of code 2020 - 2b

file = open('puzzle_input_2.txt','r')

valid = 0
# read in each line of puzzle input
for line in file:    
    #split up the relevant doodads taking into account multiple digits
    colon = line.index(':')
    low = int(line[0:1+(line[2] == '-')])
    high = int(line[line.index('-')+1:colon-1])
    char = line[colon-1]
    pwd = line[colon+2:len(line)]

    # validate: != equates to XOR which is interesting but not clear    
    valid += ((pwd[low-1]==char) != (pwd[high-1]==char)) 
    
print(valid)
    
    
    
    




