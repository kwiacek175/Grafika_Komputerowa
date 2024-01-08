import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objects.pyramid import Pyramid

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)

    pyramid = Pyramid((0, 1, 0), 1.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        pyramid.draw(quadric)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
