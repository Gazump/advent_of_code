# Boshoff
# advent of code 2020 - 4b

byr,iyr,eyr,hgt,hcl,ecl,pid,cid = 0,1,2,3,4,5,6,7
valid_hair = '0123456789abcdef'
valid_eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate(key,code):

    if key == byr:
        if code.isdigit() and int(code) >= 1920 and int(code) <= 2002:
            return True
    elif key == iyr:
        if code.isdigit() and int(code) >= 2010 and int(code) <= 2020:
            return True
    elif key == eyr:
        if code.isdigit() and int(code) >= 2020 and int(code) <= 2030:
            return True
    elif key == hgt:
        if code[-2:] == 'cm' and code[:-2].isdigit() and int(code[:-2]) >= 150 and int(code[:-2]) <= 193:
            return True
        if code[-2:] == 'in' and code[:-2].isdigit() and int(code[:-2]) >= 59 and int(code[:-2]) <= 76:
            return True
    elif key == hcl:
        if code[0] == '#' and len(code) == 7:
            for digit in code[1:]:
                if not (digit in valid_hair):
                    return False                
            return True
    elif key == ecl:
        if len(code) == 3 and (code in valid_eye):
            return True
    elif key == pid:
        if len(code) == 9 and code.isdigit():
            return True
    elif key == cid:
        return True
    
    return False

# MAIN
    
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
            if (code[0:3] == 'byr' and validate(byr,code[4:]) or
                code[0:3] == 'iyr' and validate(iyr,code[4:]) or
                code[0:3] == 'eyr' and validate(eyr,code[4:]) or
                code[0:3] == 'hgt' and validate(hgt,code[4:]) or
                code[0:3] == 'hcl' and validate(hcl,code[4:]) or
                code[0:3] == 'ecl' and validate(ecl,code[4:]) or
                code[0:3] == 'pid' and validate(pid,code[4:])):                
                present += 1            
            elif code[0:3] == 'cid':
                pass
            else:
                present -= 666
print(count)


