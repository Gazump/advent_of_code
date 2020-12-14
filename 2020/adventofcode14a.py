# Boshoff
# advent of code 2020 - 14a

lines = open('puzzle_input_14.txt','r').read().splitlines()

mem = [0]*(10**5)
mask = ''
for line in lines:
    words = line.split(' ')
    if words[0] == 'mask':
        mask = words[2]
    else:
        index = int(words[0][4:words[0].index(']')])
        num = str(bin(int(words[2])))[2:]
        num = '0'*(len(mask)-len(num))+num
        new_num = ''
        for i,x in enumerate(mask):
            if x == 'X':
                new_num += num[i]
            else:
                new_num += x
        mem[index] = int(new_num,2)
print(sum(mem))

            
            
        
        

        

    
