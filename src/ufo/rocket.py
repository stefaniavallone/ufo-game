import random

import pygame


class Rocket:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 20)
        self.image = pygame.transform.flip(pygame.image.load('../resources/rocket.png'), False, True)

    def mov_rocket(self):
        self.y += 10

    def destroy_rocket(self):
        if self.y >= 550:
            return True

    def rocket_position(self):
        self.rocket_dx = self.x + self.image.get_width()
        self.rocket_sx = self.x
        self.rocket_up = self.y
        self.rocket_down = self.y + self.image.get_height()




