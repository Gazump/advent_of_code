# Boshoff
# advent of code 2020 - 6b

lines = open('puzzle_input_6.txt','r').read().splitlines()
lines.append('')
questions, total, group_count = [0]*26, 0, 0
for line in lines:    
    if line == '':
        # end of group record
        for letter in questions:
            if letter == group_count:
                total += 1
        questions, group_count = [0]*26, 0
    else:
        group_count += 1
        for char in line:
            questions[ord(char)-97] += 1
print(total)
