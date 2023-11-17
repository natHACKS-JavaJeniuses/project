import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh

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
glTranslatef(0.0, 0.0, -10)  # Adjust translation based on the size of your model

# Main rendering loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Render the STL model
    glBegin(GL_TRIANGLES)
    for vector in mesh_data.vectors:
        for vertex in vector:
            glVertex3fv(vertex)
    glEnd()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
