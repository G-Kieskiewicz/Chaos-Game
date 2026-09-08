import numpy as np
import matplotlib.pyplot as plt
import math
import random

theta = 0
n = 4
h = 1
verticies = np.zeros((n,2) , dtype = 'float')

iterationCount = 10000
points = np.zeros((iterationCount,2), dtype = 'float')
r = 0.5

for i in range(n):
    x = math.cos(theta) * h
    y = math.sin(theta) * h
    theta = theta + ((2*math.pi)/n)
    verticies[i] = [x,y]

idx = [0, 0, 0]  # idx[0] = current pick, idx[1] = previous pick, idx[2] = pick before that

def random_point_index():
    global idx
    idx[2] = idx[1]
    idx[1] = idx[0]
    dst1 = abs(idx[1] - idx[2])

    while True:
        idx[0] = random.randint(0, n - 1)
        dst = abs(idx[0] - idx[1])
        if dst1 == 0 and (dst == 1 or dst == n - 1):
            continue
        else:
            break

    return idx[0]

for i in range(iterationCount-1):
    index = random_point_index()
    point_1 = verticies[index]
    point_2 = points[i]

    x = point_2[0] + (point_1[0] - point_2[0]) * r
    y = point_2[1] + (point_1[1] - point_2[1]) * r

    points[i+1] = [x,y]

fig, ax = plt.subplots()
ax.scatter(verticies[:,0], verticies[:,1])
ax.scatter(points[:,0], points[:,1], s=1, marker='.')
ax.set_aspect('equal')
ax.grid(True)
plt.show()