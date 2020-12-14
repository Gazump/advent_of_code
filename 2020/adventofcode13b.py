# Boshoff
# advent of code 2020 - 13b
from functools import reduce

# step 3 of chinese algorithm to find inverse
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

lines = open('puzzle_input_13.txt','r').read().splitlines()
buses = []
offsets = []

for i,bus in enumerate(lines[1].split(',')):

    if bus != 'x':
        buses.append(int(bus))
        offsets.append(int(bus)-i)

# Chinese Remainder Theorem
N = 0
prod = reduce(lambda offsets, b: offsets*b, buses)
for n_i, a_i in zip(buses, offsets):
    p = prod // n_i
    N += a_i * mul_inv(p, n_i) * p
print(N % prod)
        

    
