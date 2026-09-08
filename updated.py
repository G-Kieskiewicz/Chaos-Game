import pyvista as pv
import pygame
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

def generate_chaos_points(vertices, r, iterations):
    """Run the chaos game and return the list of generated (x, y) points."""
    current = vertices[0]
    generated = [current]
 
    for _ in range(iterations):
        idx = random_points(vertices, history)
        target = vertices[idx]
 
        x = current[0] + (target[0] - current[0]) * r
        y = current[1] + (target[1] - current[1]) * r
 
        current = (x, y)
        generated.append(current)
 
    return generated
 
 
def display_points(vertices, generated, length):
    pygame.init()
    width = height = length
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chaos Game")
    screen.fill((0, 0, 0))
 
    cx, cy = width // 2, height // 2
 
    # plot the fractal points
    for (x, y) in generated:
        px, py = int(cx + x), int(cy + y)
        if 0 <= px < width and 0 <= py < height:
            screen.set_at((px, py), (0, 255, 140))
 
    # mark the polygon vertices in red for reference
    for (x, y) in vertices:
        px, py = int(cx + x), int(cy + y)
        pygame.draw.circle(screen, (255, 60, 60), (px, py), 3)
 
    pygame.display.flip()
 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
 
    pygame.quit()
 
 
def main():
    print("=== Chaos Game ===\n")
    n = int(input("Enter number of vertices, n (>=3): "))
    r = float(input("Enter the modifier between 0 and 1, r (0...1): "))
    print("\nGenerating samples... please wait...")
 
    length = 900
    iterations = 100000
 
    vertices = initialise_polygon(length, n)
    generated = generate_chaos_points(vertices, r, iterations)
 
    print(f"Generated {len(generated)} points. Opening display window...")
    display_points(vertices, generated, length)
 
 
if __name__ == "__main__":
    main()