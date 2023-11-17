import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh
import numpy as np

# Load STL file
your_stl_file_path = "Cute_triceratops.stl"
mesh_data = mesh.Mesh.from_file(your_stl_file_path)

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
window_size = (width, height)
screen = pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)

# Set the window title
pygame.display.set_caption("STL File with OpenGL")

# Set up OpenGL perspective
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (width / height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -50)  # Adjust translation based on the size of your model

# Enable lighting
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)

# Set light position
light_position = [1, 1, 1, 0]
glLightfv(GL_LIGHT0, GL_POSITION, light_position)

# Set material properties
glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
glMaterialfv(GL_FRONT, GL_SHININESS, 100.0)

# Set initial rotation angles
angle_x, angle_y = 0, 0

# Main rendering loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle_y += 1
    if keys[pygame.K_RIGHT]:
        angle_y -= 1
    if keys[pygame.K_UP]:
        angle_x += 1
    if keys[pygame.K_DOWN]:
        angle_x -= 1

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Apply rotation
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -50)
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)

    # Render the STL model
    glBegin(GL_TRIANGLES)
    for vector in mesh_data.vectors:
        normal = np.cross(vector[1] - vector[0], vector[2] - vector[0])
        normal /= np.linalg.norm(normal)
        glNormal3fv(normal)

        for vertex in vector:
            glVertex3fv(vertex)
    glEnd()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
