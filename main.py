import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objects.sierpinskiPyramid import SierpinskiPyramid


def main(levels):
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)

    sierpinski_pyramid = SierpinskiPyramid((0, 1, 0), 1.0, levels)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        sierpinski_pyramid.draw(quadric)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    levels = int(input("Podaj liczbę poziomów piramidy Sierpińskiego: "))
    main(levels)














