import pygame
from settings import *

pygame.init() # Inicia todos los modulos (audio, imagen....)

SCREEN = pygame.display.set_mode(PANTALLA_RESOLUCION) # Resolucion del juego
pygame.display.set_caption("Dark Souls") # Nombre del juego 

clock = pygame.time.Clock()




SCREEN.fill(CUSTOM) # Color de la pantalla


contador = 0
is_running = True
while is_running:
    clock.tick(60)
    print(contador)
    contador += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.flip()

pygame.quit()