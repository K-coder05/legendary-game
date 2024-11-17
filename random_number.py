import pygame
import random
from pygame.math import Vector2

class NUMBER:
    def __init__(self, cell_number):
        self.cell_number = cell_number
        self.randomize()

    def draw_number(self, screen, cell_size, number):
        number_rect = pygame.Rect(
            int(self.pos.x * cell_size),
            int(self.pos.y * cell_size),
            cell_size,
            cell_size
        )
        screen.blit(number, number_rect)

    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)