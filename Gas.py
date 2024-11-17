import random
import pygame
import os

class Gas:
    def __init__(self, WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MAIN_WIDTH = MAIN_WIDTH
        self.MAIN_HEIGHT = MAIN_HEIGHT

        self.respawn()

    def draw_gas(self, win):
        win.blit(self.gas_img, (self.gas_rect.x, self.gas_rect.y))

    def respawn(self):
        # Generate new random position
        self.x = random.randint(0, self.WIDTH - self.MAIN_WIDTH)
        self.y = random.randint(0, self.HEIGHT - self.MAIN_HEIGHT)
        self.gas_rect = pygame.Rect(self.x, self.y, self.MAIN_WIDTH, self.MAIN_HEIGHT)
        
        # Generate new random gas can image
        random_gas_num = random.randint(0, 9)
        self.generate_random_gas(random_gas_num)

    def generate_random_gas(self, random_gas_num):
        gas_image_filename = f"Gascan{random_gas_num}.png"
        self.gas_img = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets/Numbers', gas_image_filename)),
            (self.MAIN_WIDTH, self.MAIN_HEIGHT)
        )