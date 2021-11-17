import pygame


class Ufo:
    def __init__(self):
        self.tolerance = 10
        self.x, self.y = 500, 550
        self.image = pygame.image.load('../resources/ufo.png')

    def ufo_position(self):
        self.ufo_dx = self.x + self.image.get_width() - self.tolerance
        self.ufo_sx = self.x + self.tolerance
        self.ufo_up = self.y + self.tolerance
        self.ufo_down = self.y + self.image.get_height() - self.tolerance

    def collision(self, rocket):
        rocket.rocket_position()
        if self.ufo_dx > rocket.rocket_sx and self.ufo_sx < rocket.rocket_dx \
                and self.ufo_up <= rocket.rocket_down:
            return True
