import numpy as np
import matplotlib.pyplot as plt
import math
import random

theta = 0
n = 3
h = 1
verticies = np.zeros((n,2) , dtype = 'float')

iterationCount = 1000000
points = np.zeros((iterationCount,2), dtype = 'float')
r = 0.5 # the modifier where 

for i in range(n):
    x = math.cos(theta) * h
    y = math.sin(theta) * h
    theta = theta + ((2*math.pi)/n)
    verticies[i] = [x,y]

#last_index = -1  # no previous pick yet

for i in range(iterationCount-1):
    index = random.randint(0, n-1)
    """    while index == last_index:
            index = random.randint(0, n-1)
        last_index = index
    """
    point_1 = verticies[index]
    point_2 = points[i]

    x = point_2[0] + (point_1[0] - point_2[0]) * r
    y = point_2[1] + (point_1[1] - point_2[1]) * r

    points[i+1] = [x,y]

print(verticies)
fig, ax = plt.subplots()

ax.scatter(verticies[:,0], verticies[:,1])
ax.scatter(points[:,0], points[:,1], s=1) 

# move the axes to cross at the origin
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_aspect('equal')
ax.grid(True)

plt.show()