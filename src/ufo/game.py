from enum import Enum

import pygame

from ufo.heart import Heart
from ufo.rocket import Rocket
from ufo.ufo import Ufo


class Status(str, Enum):
    START = "start",
    PAUSE = "pause",
    GAMEOVER = "gameover"
    QUIT = "quit"

class Game:
    def __init__(self):
        pygame.init()
        self.FPS = 50
        self.points = 0
        self.ufo = Ufo()
        self.screen = None
        self.heart_list = []
        self.rocket_list = []
        self.window_size = 1000, 700
        pygame.display.set_caption('Ufo Game')
        self.pause_image = pygame.image.load('../resources/pause.png')
        self.font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)
        self.background = pygame.image.load('../resources/background.jpeg')
        self.gameover_image = pygame.image.load('../resources/gameover.png')

    def inizialize(self, heart_n):
        self.heart_list = []
        self.rocket_list = []
        self.status = Status.START
        self.screen = pygame.display.set_mode(self.window_size)
        self.screen.blit(self.background, (0, 0))
        for i in range(1, 3):
            self.rocket_list.append(Rocket())
        heartx_pos = 10
        for i in range(heart_n):
            self.heart_list.append(Heart(heartx_pos, 10))
            heartx_pos += 35

    def start(self, heart_n):
        self.inizialize(heart_n)
        self.event()
        self.run()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status = Status.QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.status == Status.PAUSE:
                        self.status = Status.START
                    elif self.status == Status.START:
                        self.status = Status.PAUSE
                    else:
                        # gameover
                        if len(self.heart_list) > 1:
                            if self.points > 0:
                                self.points -= 1
                            self.start(len(self.heart_list) - 1)
                        else:
                            self.points = 0
                            self.start(3)
                if event.key == pygame.K_LEFT:
                    self.ufo.x += -20
                if event.key == pygame.K_RIGHT:
                    self.ufo.x += 20

    def run(self):
        while not self.status == Status.QUIT:
            self.event()
            if self.status == Status.START:
                if len(self.rocket_list) < 5:
                    for i in range(1, 3):
                        self.rocket_list.append(Rocket())
                self.draw_object()
            else:
                if self.status == Status.PAUSE:
                    self.pause()
                else:
                    if self.status == Status.GAMEOVER:
                        self.gameover()
                    else:
                        self.status = Status.QUIT
                        pygame.quit()

    def gameover(self):
        self.screen.blit(self.gameover_image, (400, 300))
        self.screen.blit(self.font.render("Press space to restart", 1, (255, 0, 0)), (200, 350))
        pygame.display.update()
        pygame.time.Clock().tick(self.FPS)

    def pause(self):
        self.screen.blit(self.pause_image, (400, 100))
        self.screen.blit(self.font.render("Press space to restart", 1, (255, 0, 0)), (200, 350))
        pygame.display.update()
        pygame.time.Clock().tick(self.FPS)

    def draw_object(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.ufo.image, (self.ufo.x, self.ufo.y))
        font_point = pygame.font.SysFont('Comic Sans MS', 20, bold=True)
        self.screen.blit(font_point.render("Points " + str(self.points), 1, (255, 0, 0)), (900, 5))
        for heart in self.heart_list:
            self.screen.blit(heart.image, (heart.x, heart.y))
        self.ufo.ufo_position()
        for rocket in self.rocket_list:
            rocket.mov_rocket()
            if self.ufo.collision(rocket):
                self.status = Status.GAMEOVER
                break
            if rocket.destroy_rocket():
                self.points += 1
                self.rocket_list.remove(rocket)
            self.screen.blit(rocket.image, (rocket.x, rocket.y))
        pygame.display.update()
        pygame.time.Clock().tick(self.FPS)
