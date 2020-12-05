# Boshoff
# advent of code 2019 - 4b

line = open('puzzle_input_4.txt','r').read().split('-')

count = 0
for n in range(int(line[0]),int(line[1])+1):
    double = False
    ascending = True
    for i in range(1,len(str(n))):
        if str(n)[i] < str(n)[i-1]:
            ascending = False
            break

    # beginning/end double
    if ( str(n)[0] == str(n)[1] and str(n)[0] != str(n)[2] or
         str(n)[-1] == str(n)[-2] and str(n)[-1] != str(n)[-3]):
        double = True
    # middle double only
    else:        
        for i in range(1,len(str(n))-1):
            if str(n)[i-1] != str(n)[i] and str(n)[i] == str(n)[i+1] and str(n)[i] != str(n)[i+2]:
                double = True
            
    count += double*ascending    

print(count)
        
        
            
        





