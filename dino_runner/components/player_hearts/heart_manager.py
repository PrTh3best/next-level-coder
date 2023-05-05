from msilib.schema import SelfReg
from typing import Self
from dino_runner.components.player_hearts.heart import Heart
from dino_runner.utils.constants import PYZZA_TYPE

class HeartManager:
    def __init__(self):
        self.heart_count = 5

    def reduce_heart(self):
        self.heart_count -= 1

    def draw(self, screen):
        pos_x = 10
        pos_y = 20

        for heart in range(self.heart_count):
            heart = Heart(pos_x, pos_y)
            heart.draw(screen)
            pos_x += 30

   # if Self.player(PYZZA_TYPE):
    #    SelfReg.heart_count = 2