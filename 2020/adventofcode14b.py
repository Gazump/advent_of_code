# Boshoff
# advent of code 2020 - 14b

lines = open('puzzle_input_14.txt','r').read().splitlines()

def find_combo(address):
    combos = []
    if 'X' in address:
        combos += find_combo(address.replace('X','0',1))
        combos += find_combo(address.replace('X','1',1))
        return combos
    else:
        return [address]   

mem = {}
mask = ''
for line in lines:
    words = line.split(' ')
    if words[0] == 'mask':
        mask = words[2]
    else:
        index = str(bin(int(words[0][4:words[0].index(']')])))[2:]        
        index = '0'*(len(mask)-len(index))+index
        num = int(words[2])        
        address = ''
        for i,x in enumerate(mask):
            if x == '1':              
                address += '1'
            elif x == 'X':
                address += 'X'
            else: # both x and 0
                address += index[i]
        mems = find_combo(address)        
        for index in mems:
            i = int(index,2)            
            mem[i] = num
print(sum(mem.values()))

            
            
        
        

        

    
