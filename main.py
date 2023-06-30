import pygame
from pygame.locals import *
from math import sin, cos, radians

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define cube properties
cube_pos = [width / 2, height / 2]  # Initial cube position
cube_size = 100  # Cube size

# Define cube vertices
vertices = [
    (-cube_size, -cube_size, -cube_size),
    (-cube_size, cube_size, -cube_size),
    (cube_size, cube_size, -cube_size),
    (cube_size, -cube_size, -cube_size),
    (-cube_size, -cube_size, cube_size),
    (-cube_size, cube_size, cube_size),
    (cube_size, cube_size, cube_size),
    (cube_size, -cube_size, cube_size)
]

# Define cube edges
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Define cube rotation angles
rotation_x = 0
rotation_y = 0
rotation_z = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        cube_pos[0] -= 3
    if keys[K_RIGHT]:
        cube_pos[0] += 3
    if keys[K_UP]:
        cube_pos[1] -= 3
    if keys[K_DOWN]:
        cube_pos[1] += 3

    if keys[K_w]:
        rotation_x += 2
    if keys[K_s]:
        rotation_x -= 2
    if keys[K_a]:
        rotation_y += 2
    if keys[K_d]:
        rotation_y -= 2

    # Clear the screen
    screen.fill((0, 0, 0))

    # Rotate and draw the cube
    for edge in edges:
        x1, y1, z1 = vertices[edge[0]]
        x2, y2, z2 = vertices[edge[1]]

        # Apply 3D rotation
        x1r = x1 * cos(radians(rotation_x)) - z1 * sin(radians(rotation_x))
        z1r = x1 * sin(radians(rotation_x)) + z1 * cos(radians(rotation_x))
        y1r = y1 * cos(radians(rotation_y)) - z1r * sin(radians(rotation_y))
        z1r = y1 * sin(radians(rotation_y)) + z1r * cos(radians(rotation_y))
        x1 = x1r * cos(radians(rotation_z)) + y1r * sin(radians(rotation_z))
        y1 = -x1r * sin(radians(rotation_z)) + y1r * cos(radians(rotation_z))
        z1 = z1r

        x2r = x2 * cos(radians(rotation_x)) - z2 * sin(radians(rotation_x))
        z2r = x2 * sin(radians(rotation_x)) + z2 * cos(radians(rotation_x))
        y2r = y2 * cos(radians(rotation_y)) - z2r * sin(radians(rotation_y))
        z2r = y2 * sin(radians(rotation_y)) + z2r * cos(radians(rotation_y))
        x2 = x2r * cos(radians(rotation_z)) + y2r * sin(radians(rotation_z))
        y2 = -x2r * sin(radians(rotation_z)) + y2r * cos(radians(rotation_z))
        z2 = z2r

        # Apply 2D projection
        x1, z1 = x1 * cos(radians(45)) - z1 * sin(radians(45)), x1 * sin(radians(45)) + z1 * cos(radians(45))
        x1, y1 = x1 * cos(radians(30)) + y1 * sin(radians(30)), -x1 * sin(radians(30)) + y1 * cos(radians(30))
        z1 += cube_size

        x2, z2 = x2 * cos(radians(45)) - z2 * sin(radians(45)), x2 * sin(radians(45)) + z2 * cos(radians(45))
        x2, y2 = x2 * cos(radians(30)) + y2 * sin(radians(30)), -x2 * sin(radians(30)) + y2 * cos(radians(30))
        z2 += cube_size

        # Apply cube position
        x1, y1 = x1 + cube_pos[0], y1 + cube_pos[1]
        x2, y2 = x2 + cube_pos[0], y2 + cube_pos[1]

        # Draw the edge
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
