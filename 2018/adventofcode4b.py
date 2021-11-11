# NMB
# AoC 2018
# Problem 4a

lines = sorted(open('puzzle_input_4.txt','r').read().splitlines())
grid,date,ID,minutes,rows,sleep_from = [],'02-03','509',['.']*60,[],-1
for line in lines:
    tokens = line.split(' ')
    d_tokens = tokens[0].split('-')
    new_date = d_tokens[1]+'-'+d_tokens[2]
    time = int(tokens[1][3:-1])    
    if tokens[2] == 'Guard':        
        grid.append([date,ID,minutes])
        minutes = ['.']*60
        ID = tokens[3][1:]
    elif  tokens[2] == 'falls':
        sleep_from = time
    elif tokens[2] == 'wakes':
        for c in range(sleep_from,time):
            minutes[c] = '#'
    if date != new_date:
        date = new_date
freqs,best_key,best_value,best_minute = {},'',0,-1
for row in grid:
    if row[1] not in freqs:
        freqs[row[1]] = [0]*60    
    for i in range(60):
        if row[2][i] == '#':
            freqs[row[1]][i] += 1
            if freqs[row[1]][i] > best_value:
                best_value = freqs[row[1]][i]
                best_key = row[1]
                best_minute = i               
print(int(best_key)*best_minute)

### OUTPUT TABLE
##print('Date\tID\tMinute')
##print('\t\t000000000011111111112222222222333333333344444444445555555555')
##print('\t\t012345678901234567890123456789012345678901234567890123456789')
##
##for row in grid:
##    print(row[0]+'\t'+row[1]+'\t',end='')
##    output = ''
##    for m in row[2]:
##        output += m
##    print(output)

    
    
    



 
                
