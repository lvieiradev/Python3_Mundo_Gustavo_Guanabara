import pygame

pygame.mixer.init()

pygame.mixer.music.load(r"C:\Users\lucas\OneDrive\Área de Trabalho\musica.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass