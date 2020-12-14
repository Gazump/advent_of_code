# Boshoff
# advent of code 2020 - 13a

lines = open('puzzle_input_13.txt','r').read().splitlines()
departure = int(lines[0])
take_bus = -1
min_wait = 9999999
for bus in sorted(lines[1].split(',')):    
    if bus != 'x':
        bus = int(bus)
        next_bus = ((departure // bus) + 1)*bus
        if next_bus - departure < min_wait:        
            take_bus = bus
            min_wait = next_bus - departure
    else:
        break
print(take_bus*min_wait)


        

    
