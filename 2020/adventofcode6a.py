# Boshoff
# advent of code 2020 - 6a
    
lines = open('puzzle_input_6.txt','r').read().splitlines()
lines.append('')
questions, total = [0]*26, 0
for line in lines:
    if line == '':
        total += sum(questions)
        questions = [0]*26
    else:
        for char in line:
            questions[ord(char)-97] = 1
print(total)
