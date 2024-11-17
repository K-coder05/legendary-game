import random, pygame, os

class Gas:
    def __init__(self, WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MAIN_WIDTH = MAIN_WIDTH
        self.MAIN_HEIGHT = MAIN_HEIGHT

        self.x = random.randint(0, self.WIDTH - self.MAIN_WIDTH)
        self.y = random.randint(0, self.HEIGHT - self.MAIN_HEIGHT)
        self.gas_rect = pygame.Rect(self.x, self.y, self.MAIN_WIDTH, self.MAIN_HEIGHT)
        self.gas_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'gas.png')), (self.MAIN_WIDTH, self.MAIN_HEIGHT))


    def draw_gas(self, win):
        win.blit(self.gas_img, (self.gas_rect.x, self.gas_rect.y))

    def respawn(self):
        self.x = random.randint(0, self.WIDTH - self.MAIN_WIDTH)
        self.y = random.randint(0, self.HEIGHT - self.MAIN_HEIGHT)
        self.gas_rect = pygame.Rect(self.x, self.y, self.MAIN_WIDTH, self.MAIN_HEIGHT)
        