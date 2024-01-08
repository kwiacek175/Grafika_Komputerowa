import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objects.sierpinskiPyramid import SierpinskiPyramid

# Zmienne do śledzenia pozycji kamery
camera_x = 0.0
camera_y = 0.0
camera_zoom = -3.0
rotation_angle = 0.5  # Początkowy kąt obrotu
rotation_speed = 0.5  # Szybkość obrotu

def main(levels):

    global camera_x, camera_y, camera_zoom, rotation_angle, rotation_speed

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, camera_zoom)

    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)

    sierpinski_pyramid = SierpinskiPyramid((0, 1, 0), 1.0, levels)

    # Dodanie świateł
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Źródło światła kierunkowe
    glEnable(GL_LIGHT1)  # Źródło światła punktowe

    # Źródło światła kierunkowe
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])

    # Źródło światła punktowe
    glLightfv(GL_LIGHT1, GL_POSITION, [0, 0, 5, 1])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1, 1, 1, 1])  # Kolor światła punktowego

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()
            # Obsługa przesuwania kamery
            if keys[K_LEFT]:
                camera_x += 0.01
            elif keys[K_RIGHT]:
                camera_x -= 0.01
            elif keys[K_UP]:
                camera_y -= 0.01
            elif keys[K_DOWN]:
                camera_y += 0.01
            # Obsługa zoomowania
            elif keys[K_PLUS] or keys[K_KP_PLUS]:
                camera_zoom += 0.1
            elif keys[K_MINUS] or keys[K_KP_MINUS]:
                camera_zoom -= 0.1

        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(-camera_x, -camera_y, camera_zoom)

        # Powolne Obracanie się
        glRotatef(rotation_angle, 3, 1, 1)
        rotation_angle += rotation_speed

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        sierpinski_pyramid.draw(quadric)

        pygame.display.flip()
        pygame.time.wait(10)
        clock.tick(30)  # Ograniczenie do 30 klatek na sekundę dla płynności

if __name__ == "__main__":
    levels = int(input("Podaj liczbę poziomów piramidy Sierpińskiego: "))
    main(levels)














