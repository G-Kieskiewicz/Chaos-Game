import pyvista as pv
import matplotlib.pyplot as plt
import math
import random

history = [0,0,0] # index 0 = current point, index 1 = previous point, index 2 = 2 points before current

# let width == height so we take in length
def initialise_polygon(length, n):
    d_theta = (2*math.pi)/n
    radius = length/2 -10
    points = []

    for i in range(0,n):
        theta = i * d_theta
        points.append((radius*math.sin(theta),radius*math.cos(theta)))
    return points

def random_points(points,history):
    if len(points) <= 3:
        return random.randint(0,len(points)-1)
    history[2] = history[1]
    history[1] = history[0]
    distance1 = abs(history[1] - history[2])

    while True:
        history[0] = random.randint(0, len(points) - 1)
        distance_2 = abs(history[0] - history[1])
        if distance1 == 0 and (distance_2 == 1 or distance_2 ==  len(points) - 1):
            continue
        else:
            break
    return history[0]

"""test = random_points([1,2,3,4,5],history)
print(test)"""

def main():
    print("=== Chaos Game ===\n")
    n = int(input("Enter number of verticies, n (>=3): "))
    r = float(input("Enter the modifier between 0 and 1, r (0...1)"))
    print("\nGenerating samples... please wait...")

    length = 100
    points = initialise_polygon(length, n)

    for i in range(n,100000):
        idx = random_points(points, history)
        point_1 = points[idx]
        point_2 = points[i]

        x = point_2[0] + (point_1[0] - point_2[0]) * r
        y = point_2[1] + (point_1[1] - point_2[1]) * r

        points[i+1].append((x,y))

    print(points)

if __name__ == "__main__":
    main()