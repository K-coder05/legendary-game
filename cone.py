import random
import pygame
import os

class Cone:
    def __init__(self, WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MAIN_WIDTH = MAIN_WIDTH
        self.MAIN_HEIGHT = MAIN_HEIGHT

        self.respawn()

    def draw(self, win):
        win.blit(self.img, (self.rect.x, self.rect.y))

    def respawn(self):
        # Generate new random position
        self.x = random.randint(100, self.WIDTH - 100)
        self.y = random.randint(200, self.HEIGHT - self.MAIN_HEIGHT)
        self.rect = pygame.Rect(self.x, self.y, self.MAIN_WIDTH, self.MAIN_HEIGHT)
        
        self.generate_image()

    def generate_image(self):
        self.img = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'lebron.png')), (self.MAIN_WIDTH, self.MAIN_HEIGHT))