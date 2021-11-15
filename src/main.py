
import pygame

from ufo.Ufo import Ufo
from ufo.Heart import Heart
from ufo.Rocket import Rocket
from ufo.Constants import  Constants

pygame.init()
pygame.display.set_caption('Ufo Game')

font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

def start(heartx, heart_n):
    global screen, rocket_list, ufo, heart_list
    screen = pygame.display.set_mode(Constants.windowSize)
    screen.blit(Constants.background, (0, 0))
    screen.blit(Constants.ufo_image, (Constants.ufox, Constants.ufoy))
    heart_list = []
    rocket_list = []
    ufo = Ufo(Constants.ufox, Constants.ufoy)
    for i in range(1, 3):
        rocket_list.append(Rocket())
    for i in range(heart_n):
        heart_list.append(Heart(heartx, 10))
        heartx += 35

def draw_object(ufo, rocket_list):
    screen.blit(Constants.background, (0, 0))
    screen.blit(Constants.ufo_image, (ufo.ufox, ufo.ufoy))
    font_point = pygame.font.SysFont('Comic Sans MS', 20, bold=True)
    screen.blit(font_point.render("Points " + str(Constants.points), 1, (255, 0, 0)), (900, 5))
    for heart in heart_list:
        screen.blit(Constants.heart_image, (heart.heartx, heart.hearty))
    ufo.ufo_position(Constants.tolerance, Constants.ufo_image)
    for rocket in rocket_list:
        rocket.mov_rocket()
        if ufo.collisione(rocket, Constants.rocket_image):
            ufo.status = "gameover"
            break
        if rocket.destroy_rocket():
            Constants.points += 1
            rocket_list.remove(rocket)
        screen.blit(Constants.rocket_image, (rocket.rocketx, rocket.rockety))
    pygame.display.update()
    pygame.time.Clock().tick(Constants.FPS)

def gameover(heartx):
    screen.blit(Constants.gameover_image, (400, 300))
    screen.blit(font.render("Press space to restart", 1, (255, 0, 0)), (200, 350))
    Constants.play = False
    pygame.display.update()
    pygame.time.Clock().tick(Constants.FPS)
    while not Constants.play:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                if len(heart_list)>1:
                    if Constants.points > 0:
                        Constants.points -= 1
                    start(heartx, len(heart_list)-1)
                else:
                    Constants.points = 0
                    start(heartx, Constants.heart_n)
                Constants.play = True
            if event.type == pygame.QUIT:
                pygame.quit()

def pause():
    screen.blit(Constants.pause_image, (400, 100))
    screen.blit(font.render("Press space to restart", 1, (255, 0, 0)), (200, 350))
    pygame.display.update()
    pygame.time.Clock().tick(Constants.FPS)
    Constants.play = False
    while not Constants.play:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                start(Constants.heartx, Constants.heart_n)
                Constants.play = True
            if event.type == pygame.QUIT:
                pygame.quit()

start(Constants.heartx, Constants.heart_n)

while Constants.play:
    if (ufo.status == "start"):
        ufo = Ufo(Constants.ufox, Constants.ufoy)
        Constants.ufox = ufo.ufox
        Constants.ufoy = ufo.ufoy
        if len(rocket_list) < 5:
            for i in range(1, 3):
                rocket_list.append(Rocket())
        draw_object(ufo, rocket_list)
    else:
        if (ufo.status == "pause"):
            pause()
        else:
            if ufo.status == "gameover":
                gameover(Constants.heartx)
            else:
                pygame.quit()