# NMB
# Advent of Code 2021
# Problem 08b

lines = open('input_08.txt','r').read().splitlines()
total = 0
for line in lines:
    # count occurances of lines
    counts = {}
    wires = line.split(' | ')
    for c in 'abcdefg':
        freq = wires[0].count(c)
        if freq in counts:
            counts[freq].append(c)
        else:
            counts[freq] = [c]
    two, three = 'z', 'z'
    for w in wires[0].split(' '):
        if len(w) == 2:
            two = w
        elif len(w) == 3:
            three = w
    # map count of lines to correct a-g
    e, c = counts[4][0], 'z'
    maps = {e:'e', counts[6][0]:'b', counts[9][0]:'f', set(two).symmetric_difference(set(three)).pop():'a'}
    for n in counts[8]:
        if n not in maps:
            maps[n] = 'c'
            c = n
            break
    for w in wires[0].split(' '):
        if len(w) == 6 and (c in w and e in w):
            for char in w:
                if char not in maps:                    
                    maps[char] = 'g'
                    break
    for c in 'abcdefg':
        if c not in maps:
            maps[c] = 'd'
            break
    # match codes for output values
    nums = ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
    answer = ''
    for digits in wires[1].split(' '):
        code = []
        for digit in digits:
            for c in digit:
                code.append(maps[c])
        answer += str(nums.index(''.join(sorted(code))))
    total += int(answer)
print(total)   

    



        
        



    
        
                        
                        
                        
                        


            
    
        
                        

