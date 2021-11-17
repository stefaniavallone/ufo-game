import pygame


class Heart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('../resources/heart.png')
