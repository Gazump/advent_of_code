# NMB
# AoC 2018
# Problem 5a

polymer = open('puzzle_input_5.txt','r').read()
reduced = ''
isChanged = True

while isChanged:    
    isChanged = False
    i = 0
    while i < len(polymer)-1:
        if polymer[i] != polymer[i+1] and polymer[i].upper() == polymer[i+1].upper():
            isChanged = True
            i += 1
        else:            
            reduced += polymer[i]
            if i == len(polymer)-2:
                reduced += polymer[i+1]
        i += 1
    polymer = str(reduced)
    reduced = ''    
print(len(polymer))
    
