import pygame, sys, random
from pygame.math import Vector2

class CAR:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)

    def draw_car(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size) 
            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    def move_car(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def boost_speed(self):
        self.direction = Vector2(2, 0)

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(number, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class SCOREBOARD:
    def __init__(self):
        self.score = 0
        self.target_score = random.randint(0, 9)
    
    def add_point(self):
        self.score += 1
        print(self.score)

    def get_score(self):
        return self.score

    def get_target(self):
        return self.target_score


class MAIN:
    def __init__(self):
        self.car = CAR()
        self.fruit = FRUIT()
        self.score = SCOREBOARD()

    def update(self):
        self.car.move_car()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.car.draw_car()

    def check_collision(self):
        if self.fruit.pos == self.car.body[0]:
            self.fruit.randomize()
            self.score.add_point()
            if self.score.get_score() >= self.score.get_target():
                self.game_over()

    def check_fail(self):
        # check if car is outside of screen
        if not 0 <= self.car.body[0].x < cell_number or not 0 <= self.car.body[0].y < cell_number:
            self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
            

pygame.init()

cell_size = 40
cell_number = 20


screen = pygame.display.set_mode((cell_number *  cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
number = pygame.image.load('Assets/lebron.png').convert_alpha()


fruit = FRUIT()
car = CAR()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.car.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                main_game.car.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                main_game.car.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                main_game.car.direction = Vector2(1, 0)

            
    
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
