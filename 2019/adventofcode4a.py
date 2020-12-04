# Boshoff
# advent of code 2019 - 4a

line = open('puzzle_input_4.txt','r').read().split('-')

count = 0
for n in range(int(line[0]),int(line[1])+1):
    double = False
    ascending = True
    for i in range(1,len(str(n))):
        if str(n)[i] < str(n)[i-1]:
            ascending = False
            break
        elif str(n)[i] == str(n)[i-1]:
            double = True
    count += double*ascending
    

print(count)
        
        
            
        





