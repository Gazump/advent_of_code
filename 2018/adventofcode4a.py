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
counts = {}
for row in grid:
    if row[1] in counts:
        counts[row[1]] += row[2].count('#')
    else:
        counts[row[1]] = row[2].count('#')
sleepy = max(counts,key=counts.get)
freq = [0]*60
for row in grid:
    if row[1] == sleepy:
        for i in range(60):
            if row[2][i] == '#':
                freq[i] += 1
print(int(sleepy)*freq.index(max(freq)))

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

    
    
    



 
                
