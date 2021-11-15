import pygame

class Constants:
    FPS = 50
    points = 0
    play = True
    heartx = 10
    heart_n = 3
    tolerance = 1
    ufox, ufoy = 500, 550
    windowSize = 1000, 700
    ufo_image = pygame.image.load('../resources/ufo.png')
    pause_image = pygame.image.load('../resources/pause.png')
    heart_image = pygame.image.load('../resources/heart.png')
    heart_image_ko = pygame.image.load('../resources/heart_ko.png')
    background = pygame.image.load('../resources/background.jpeg')
    gameover_image = pygame.image.load('../resources/gameover.png')
    rocket_image = pygame.transform.flip(pygame.image.load('../resources/rocket.png'), False, True)