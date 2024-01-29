import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from objects.sierpinskiPyramid import SierpinskiPyramid

# Zmienne do śledzenia pozycji kamery
camera_x = 0.0
camera_y = 0.0
camera_zoom = -3.0
rotation_angle = 0.5  # Początkowy kąt obrotu
rotation_speed = 1  # Szybkość obrotu
textures_enabled = False
current_texture_index = 0
textures = ["texture.jpg", "texture2.jpg", "texture3.jpg"]

def toggle_textures():
    global textures_enabled
    textures_enabled = not textures_enabled
def load_texture(filename):
    img = Image.open(filename)
    img_data = img.tobytes("raw", "RGB", 0, -1)
    width, height = img.size
    return img_data, width, height

def next_texture():
    global current_texture_index
    current_texture_index = (current_texture_index + 1) % len(textures)

def set_lights():
    # Światło kierunkowe
    glLightfv(GL_LIGHT0, GL_POSITION, [0, -1, 0, 0])  # Światło padające w dół
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.0, 0.0, 1.0, 1.0])  # Niebieskie światło

    # Światło punktowe
    glLightfv(GL_LIGHT1, GL_POSITION, [0, 2, 2, 1])  # Pozycja światła punktowego
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 1.0, 0.0, 1.0])  # Żółte światło

def main(levels):

    global camera_x, camera_y, camera_zoom, rotation_angle, rotation_speed, texture_enabled

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, camera_zoom)

    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)

    sierpinski_pyramid = SierpinskiPyramid((0, 1, 0), 1.0, levels)

    # Ładowanie tekstur
    textures_data = [load_texture(filename) for filename in textures]
    glGenTextures(len(textures_data))

    for i, (texture_data, texture_width, texture_height) in enumerate(textures_data):
        glBindTexture(GL_TEXTURE_2D, i)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, texture_width, texture_height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    glEnable(GL_TEXTURE_2D)  # Włączenie obsługi tekstur

    # Dodanie świateł
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Źródło światła kierunkowe
    glEnable(GL_LIGHT1)  # Źródło światła punktowe

    # Ustawienie świateł
    set_lights()

    clock = pygame.time.Clock()

    # Ustawienie powtarzania klawiszy
    pygame.key.set_repeat(50, 10)  # argumenty: opóźnienie, przerwa

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    toggle_textures()
                elif textures_enabled and event.key == pygame.K_n:
                    next_texture()

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
        if keys[K_PLUS] or keys[K_KP_PLUS]:
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

        if textures_enabled:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, current_texture_index)
        else:
            glDisable(GL_TEXTURE_2D)

        # Rysowanie piramidy
        glPushMatrix()
        sierpinski_pyramid.draw(quadric)
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)
        clock.tick(30)  # Ograniczenie do 30 klatek na sekundę dla płynności


if __name__ == "__main__":
    levels = int(input("Podaj liczbę poziomów piramidy Sierpińskiego: "))
    main(levels)





























