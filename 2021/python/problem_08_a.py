# NMB
# Advent of Code 2021
# Problem 08a

lines = open('input_8.txt','r').read().splitlines()

c = 0
for line in lines:
    tokens = line.split(' | ')
    for signal in tokens[1].split(' '):
        if len(signal) == 2 or len(signal) == 3 or len(signal) == 4 or len(signal) == 7:
            c += 1
print(c)





    



        
        



    
        
                        
                        
                        
                        


            
    
        
                        

