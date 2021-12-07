# NMB
# Advent of Code 2021
# Problem 03b

lines = open('input_3.txt','r').read().splitlines()

def getOx(nums, j):
    c0,c1 = 0, 0
    for i in range(len(nums)):
        if nums[i][j] == '1':
            c1 += 1
        else:
            c0 += 1
    new_nums = []
    for n in nums:        
        if (c1 >= c0 and n[j] == '1') or (c0 > c1 and n[j] == '0'):
            new_nums.append(n)
    if len(new_nums) == 1:
        return new_nums[0]
    else:
        return getOx(new_nums, j+1)
        
def getCO2(nums, j):
    c0,c1 = 0, 0
    for i in range(len(nums)):
        if nums[i][j] == '1':
            c1 += 1
        else:
            c0 += 1
    new_nums = []
    for n in nums:        
        if (c0 <= c1 and n[j] == '0') or (c1 < c0 and n[j] == '1'):
            new_nums.append(n)
    if len(new_nums) == 1:
        return new_nums[0]
    else:
        return getCO2(new_nums, j+1)        

o = getOx(lines,0)
c = getCO2(lines,0)
print(int(o,2)*int(c,2))
        
