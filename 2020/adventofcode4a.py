# Boshoff
# advent of code 2020 - 4a

byr,iyr,eyr,hgt,hcl,ecl,pid,cid = 0,1,2,3,4,5,6,7

lines = open('puzzle_input_4.txt','r').read().splitlines()
lines.append('')

count = 0
present = 0

for line in lines:
    if line == '' and present == 7:
        count += 1
        present = 0
    elif line == '':
        present = 0
    else:
        for code in line.split(' '):
            if (code[0:3] == 'byr' or
                code[0:3] == 'iyr' or
                code[0:3] == 'eyr' or
                code[0:3] == 'hgt' or
                code[0:3] == 'hcl' or
                code[0:3] == 'ecl' or
                code[0:3] == 'pid'):
                present += 1            
            elif code[0:3] == 'cid':
                pass
            else:
                present -= 666
print(count)


