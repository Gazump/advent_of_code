# NMB
# Advent of Code 2021
# Problem 03b

# NOTE: Will not run in IDLE! Please execute in Terminal/CMD to see output.

from rich import print
from time import sleep

lines = open('~/../../input_3.txt','r').read().splitlines()

def getOx(nums, j):
    c0,c1 = 0, 0
    for i in range(len(nums)):
        if nums[i][j] == '1':
            c1 += 1
        else:
            c0 += 1
    new_nums = []
    print("\n\nOXYGEN INDEX:",j)
    for i, n in enumerate(nums):        
        if (c1 >= c0 and n[j] == '1') or (c0 > c1 and n[j] == '0'):
            new_nums.append(n)
            print(n[:j]+"[bold red]"+n[j]+"[/bold red]"+n[j+1:],end=' ')
        else:
            print("[white]"+n+"[/white]",end=' ')
        if (i+1) % 8 == 0:
            print()
    sleep(2)
    if len(new_nums) == 1:
        print("\n\nOxygen generator rating:  bin = [bold red]"+new_nums[0]+"[/bold red] dec = [bold red]"+str(int(new_nums[0],2))+"[/bold red]")
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
    print("\n\nCO2 INDEX:",j)
    for i, n in enumerate(nums):        
        if (c0 <= c1 and n[j] == '0') or (c1 < c0 and n[j] == '1'):
            new_nums.append(n)
            print(n[:j]+"[bold yellow]"+n[j]+"[/bold yellow]"+n[j+1:],end=' ')
        else:
            print("[white]"+n+"[/white]",end=' ')
        if (i+1) % 8 == 0:
            print()
    sleep(2)
    if len(new_nums) == 1:
        print("\n\nCO2 scrubber rating:  bin = [bold yellow]"+new_nums[0]+"[/bold yellow] dec = [bold yellow]"+str(int(new_nums[0],2))+"[/bold yellow]")
        return new_nums[0]
    else:
        return getCO2(new_nums, j+1)        

o = getOx(lines,0)
sleep(4)
c = getCO2(lines,0)
sleep(4)
print("\nOxygen Generator Rating: [bold red]"+str(int(o,2))+"[/bold red]")
print("CO2 Scrubber Rating: [bold yellow]"+str(int(c,2))+"[/bold yellow]")
print("Life Support Rating: [bold orange]"+str(int(o,2)*int(c,2))+"[/bold orange]")
        
