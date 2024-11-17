import pygame
import os
import random

class Chaser():
    def __init__(self, WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT, VEL):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__MAIN_WIDTH = MAIN_WIDTH
        self.__MAIN_HEIGHT = MAIN_HEIGHT
        self.__VEL = VEL

        self.respawn()

    def generate_direction(self, position_to_chase):
        self.__direction = self.chase_mechanic(position_to_chase)

    def generate_image(self):
        if self.__direction == 0:
            self.__image = pygame.image.load(os.path.join('Assets/ChaserSprite', 'police_east.png'))
        elif self.__direction == 1:
            self.__image = pygame.image.load(os.path.join('Assets/ChaserSprite', 'police_west.png'))
        elif self.__direction == 2:
            self.__image = pygame.image.load(os.path.join('Assets/ChaserSprite', 'police_north.png'))
        else:
            self.__image = pygame.image.load(os.path.join('Assets/ChaserSprite', 'police_south.png'))

    def chase_mechanic(self, position_to_chase):
        distance_x = abs(position_to_chase.x - self.__position_x)
        distance_y = abs(position_to_chase.y - self.__position_y)

        if distance_x > distance_y:
            if (position_to_chase.x < self.__position_x):
                self.__position_x -= self.__VEL
                return 1
            else:
                self.__position_x += self.__VEL
                return 0
        else:
            if (position_to_chase.y < self.__position_y):
                self.__position_y -= self.__VEL
                return 3
            else:
                self.__position_y += self.__VEL
                return 2
            
    def respawn(self):
        self.__position_x = random.randint(0, self.__WIDTH - self.__MAIN_WIDTH)
        self.__position_y = random.randint(500, self.__HEIGHT - (self.__MAIN_HEIGHT * 2))

    def draw(self, window, position_to_chase):
        # Generate features
        self.generate_direction(position_to_chase)
        self.generate_image()

        self.chaser_rect = pygame.Rect(self.__position_x, self.__position_y, self.__MAIN_WIDTH, self.__MAIN_HEIGHT)
        sprite = pygame.transform.scale(self.__image, (self.__MAIN_WIDTH, self.__MAIN_HEIGHT))
        window.blit(sprite, (self.chaser_rect.x, self.chaser_rect.y))

    def get_rect(self):
        return self.chaser_rect