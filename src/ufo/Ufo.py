import pygame


class Ufo():
    def __init__(self, ufox, ufoy):
        self.status = "start"
        self.ufox = ufox
        self.ufoy = ufoy
        self.jump = 10
        self.isJump = False
        self.event()

    def collisione(self, rocket, rocket_image):
        rocket.rocket_position(rocket_image)
        if self.ufo_dx > rocket.rocket_sx and self.ufo_sx < rocket.rocket_dx and self.ufo_up <= rocket.rocket_down:
            return True

    def ufo_position(self, tolerance, ufoImage):
        self.ufo_dx = self.ufox + ufoImage.get_width() - tolerance
        self.ufo_sx = self.ufox + tolerance
        self.ufo_up = self.ufoy + tolerance
        self.ufo_down = self.ufoy + ufoImage.get_height() - tolerance

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status = 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.status = 'pause'
                if event.key == pygame.K_LEFT:
                    self.ufox += -20
                if event.key == pygame.K_RIGHT:
                    self.ufox += 20
