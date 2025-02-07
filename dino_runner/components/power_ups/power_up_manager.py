import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.pyzza import Pyzza

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0


    def generate_power_ups(self, points):
        self.points = points

        if len(self.power_ups) == 0:
            type = random.randint(0, 1)
            if type == 0: 
                if self.when_appears == self.points:
                    print("generating power up")
                    self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                    self.power_ups.append(Shield())
            if type == 1:
                if self.when_appears == self.points:
                    print("generating power up")
                    self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                    self.power_ups.append(Hammer())

            if type == 1:
                if self.when_appears == self.points:
                    print("generating power up")
                    self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                    self.power_ups.append(Pyzza())

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                player.shield = True
                player.type = power_up.type

                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = start_time + (time_random * 1000)

                self.power_ups.remove(power_up)
                
            elif player.dino_rect.colliderect(power_up.rect):
                player.Hammer = True
                player.type = power_up.type

                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.Hammer_time_up = start_time + (time_random * 1000)

                self.power_ups.remove(power_up)
                
            else:
                player.dino_rect.colliderect(power_up.rect)
                player.Pyzza = True
                player.type = power_up.type

                start_time = pygame.time.get_ticks()
                time_random = random.randrange(4, 9)
                player.Pyzza_time_up = start_time + (time_random * 1000)

                self.power_ups.remove(power_up)




    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

