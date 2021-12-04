# NMB
# Advent of Code 2021
# Problem 01a

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


lines = open('input_1.txt','r').read().splitlines()
print(len(lines))
h = [int(x) for x in lines]

h_map = np.zeros((4000,4000), dtype = int)

for y in range(len(h_map)):
    for x in range(len(h_map[0])):
        #index = max(abs(2000-x),abs(2000-y))
        index = int(np.sqrt((2000-x)**2+(2000-y)**2))
        if index >= 2000:
            index = 0
        #print(index)
        h_map[y, x] = h[index]

x, y = np.meshgrid(range(h_map.shape[0]), range(h_map.shape[1]))

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, h_map)
plt.title('Advent of Code - 3D depth map')
plt.show()

# show hight map in 2d
plt.figure()
plt.title('Advent of Code - 2D depth map')
p = plt.imshow(h_map)
plt.colorbar(p)
plt.show()


  
    
