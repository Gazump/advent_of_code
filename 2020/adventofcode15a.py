# Boshoff
# advent of code 2020 - 15a

nums = open('puzzle_input_15.txt','r').read().split(',')

track = {}

for i,num in enumerate(nums):
    track[int(num)] = [i+1,-1]

c = len(nums) + 1
last = int(nums[-1])
this = -1
while c <= 2020:
    if track[last][1] == -1:
        # last was new, so 0
        this = 0
        track[0][1] = track[0][0]
        track[0][0] = c
        last = this
    else:
        #repeated so work out diff
        this = track[last][0] - track[last][1]
        if this in track:
            track[this][1] = track[this][0]
            track[this][0] = c            
        else:
            track[this] = [c, -1]
        last = this
    c += 1
print(last)


            
            
        
        

        

    
