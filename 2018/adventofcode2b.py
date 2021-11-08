# NMB
# AoC 2018
# Problem 2a
lines = open('puzzle_input_2.txt','r').read().splitlines()

def findMatch():
    for i, line in enumerate(lines):
        for j in range(i,len(lines)):            
            mismatches = 0
            for c in range(len(line)):            
                if line[c] != lines[j][c]:
                    mismatches += 1
                    mis_index = c
                    if mismatches > 1:
                        break                
            if mismatches == 1:
                return line[:mis_index]+line[mis_index+1:]

print(findMatch())
                

                
    







        

    
        
    

