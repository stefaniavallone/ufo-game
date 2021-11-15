import random


class Rocket():
    def __init__(self):
        self.rocketx = random.randint(0, 1000)
        self.rockety = random.randint(0, 20)

    def mov_rocket(self):
        self.rockety += 10

    def destroy_rocket(self):
        if self.rockety >= 550:
            return True

    def rocket_position(self, rocketImage):
        self.rocket_dx = self.rocketx + rocketImage.get_width()
        self.rocket_sx = self.rocketx
        self.rocket_up = self.rockety
        self.rocket_down = self.rockety + rocketImage.get_height()




