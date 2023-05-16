import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sierpinski Triangle")

# Set the background color
background_color = (255, 255, 255)

# Set the colors for the triangle and the points
triangle_color = (0, 0, 0)
point_color = (255, 0, 0)

# Set the number of points to generate
num_points = 50000

# Set the initial point inside the triangle
point = [width / 2, height / 2]

# Set the three vertices of the triangle
vertices = [(width / 2, 50), (50, height - 50), (width - 50, height - 50)]

# Generate the Sierpinski Triangle
for _ in range(num_points):
    vertex = random.choice(vertices)
    point[0] = (point[0] + vertex[0]) / 2
    point[1] = (point[1] + vertex[1]) / 2
    pygame.draw.circle(window, point_color, (int(point[0]), int(point[1])), 1)

    pygame.display.update()

# Draw the triangle
pygame.draw.polygon(window, triangle_color, vertices, 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set the background color
    window.fill(background_color)

    # Draw the triangle
    pygame.draw.polygon(window, triangle_color, vertices, 1)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
