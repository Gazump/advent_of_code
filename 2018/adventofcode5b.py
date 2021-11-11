# NMB
# AoC 2018
# Problem 5b

polymer = open('puzzle_input_5.txt','r').read()
minChar = ''
minCount = 0
for c in 'abcdefghijklmnopqrstuvwxyz':
    reduced = ''
    isChanged = True
    test = polymer.replace(c,"")
    test = test.replace(c.upper(),"")    
    while isChanged:    
        isChanged = False
        i = 0
        while i < len(test)-1:
            if test[i] != test[i+1] and test[i].upper() == test[i+1].upper():
                isChanged = True
                i += 1
            else:            
                reduced += test[i]
                if i == len(test)-2:
                    reduced += test[i+1]
            i += 1
        test = str(reduced)
        reduced = ''        
    if len(test) < minCount:
        minCount = len(test)
        minChar = c
print(minChar,minCount)

    
