import pygame
import os
import screen_change
import random

from gas import Gas 
from chaser import Chaser

pygame.init()

# Initialize the game
WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Legendary Game")

# Define constant variables
FPS = 60
VEL = 5
VEL_CHASE = 1
MAIN_WIDTH, MAIN_HEIGHT = 80, 60
FONT = pygame.font.Font("Assets/Turok.ttf", 32)
NUM_OF_GAS_CANS = 4
BORDER_THICKNESS = 75
BORDER_MAX_HEIGHT = 150
CLOCK = pygame.time.Clock()
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

# temp 
NUM_OF_CHASERS = 2

# Define global variables
list_of_operations = ["addition", "subtraction"]
current_operation = list_of_operations[0]
score = 0
target_score = random.randint(10, 20)
game_score = 0
position = pygame.Rect(200, 200, MAIN_WIDTH, MAIN_HEIGHT)
gas_spawns = [Gas(WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT) for i in range(NUM_OF_GAS_CANS)]
direction = 0 # 0 = right, 1 = left, 2 = up, 3 = down
start_time = pygame.time.get_ticks()
chasers = [Chaser(WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT, VEL_CHASE) for i in range(NUM_OF_CHASERS)]

# Resets the game
def reset():
    global chasers, score, target_score, position
    global gas_spawns, direction, start_time, VEL_CHASE, VEL, current_operation, game_score
    score = 0
    target_score = random.randint(10, 20)
    game_score = 0
    current_operation = "addition"
    VEL_CHASE = 1
    VEL = 5
    position = pygame.Rect(200, 200, MAIN_WIDTH, MAIN_HEIGHT)
    gas_spawns = [Gas(WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT) for i in range(NUM_OF_GAS_CANS)]
    chasers = [Chaser(WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT, VEL_CHASE) for i in range(NUM_OF_CHASERS)]
    direction = 0 # 0 = right, 1 = left, 2 = up, 3 = down
    start_time = pygame.time.get_ticks()

def draw_text(text, font, text_color, x_offset, y_offset):
    img = font.render(text, True, text_color)
    img_rect = img.get_rect(center=(WIDTH / 2 + x_offset, HEIGHT / 2 + y_offset))
    WIN.blit(img, img_rect)

def draw_score(score, font, text_color, x, y):
    score = font.render(str(score), False, text_color)
    WIN.blit(score, (x, y))

def draw_target_score(target_score, font, text_color, x, y):
    target_score_prompt = font.render(str(target_score), True, text_color)
    WIN.blit(target_score_prompt, (x, y))

def draw_game_scoreboard(game_score, font, text_color, x, y):
    game_scoreboard = font.render(str(game_score), False, text_color)
    WIN.blit(game_scoreboard, (x, y))

def draw_operation_symbol(current_operation, x, y):
    symbol_image_path = os.path.join('Assets', f"{current_operation} symbol.png")
    operation_img = pygame.image.load(symbol_image_path).convert_alpha()
    operation_img = pygame.transform.scale(operation_img, (50, 50))
    WIN.blit(operation_img, (x, y))

def draw_window(position, direction, elapsed_time):
    
    # Global variables
    global score, target_score, gas_spawns, current_operation, game_score
    
    # Load image
    if direction == 0:
        car_image = pygame.image.load(os.path.join('Assets/CarSprite', 'car_east.png'))
    elif direction == 1:
        car_image = pygame.image.load(os.path.join('Assets/CarSprite', 'car_west.png'))
    elif direction == 2:
        car_image = pygame.image.load(os.path.join('Assets/CarSprite', 'car_north.png'))
    else:
        car_image = pygame.image.load(os.path.join('Assets/CarSprite', 'car_south.png'))

    mainSprite = pygame.transform.scale(car_image, (MAIN_WIDTH, MAIN_HEIGHT))

    background_image = pygame.image.load(os.path.join('Assets', 'background.png')).convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    elapsed_time = round(elapsed_time, 2)
    timer_text = f"Time: {elapsed_time}s"
    timer_surface = FONT.render(timer_text, False, WHITE)

    WIN.blit(background_image, (0, 0))
    WIN.blit(mainSprite, (position.x, position.y))
    WIN.blit(timer_surface, (800, 100))

    for gas_spawn in gas_spawns:
        if position.colliderect(gas_spawn.gas_rect):
            if current_operation == "subtraction":
                score -= gas_spawn.random_gas_num
            elif current_operation == "addition":
                score += gas_spawn.random_gas_num
            gas_spawn.respawn()
        gas_spawn.draw_gas(WIN)

    for chaser in chasers:
        chaser.draw(WIN, position)
        
    draw_score("Score: " + str(score), FONT, WHITE, 100, 100)
    draw_target_score("Target Score: " + str(target_score), FONT, WHITE, 350, 100)
    if current_operation == "addition":
        draw_operation_symbol(current_operation, 250, 100)
    elif current_operation == "subtraction":
        draw_operation_symbol(current_operation, 250, 100)
    draw_game_scoreboard("Points: " + str(game_score), FONT, WHITE, 900, 10)

def main():
    

    # Tell interpreter to find global variables
    global score, target_score, position, gas_spawns, chasers
    global direction, start_time, VEL_CHASE, VEL, current_operation, game_score  

    run = screen_change.main_screen()
    if run:
        run = screen_change.controls_screen()

    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = screen_change.pause_screen()

        # Define the movement of the character
        if direction == 0:
            position.x += VEL
            if position.x + VEL + MAIN_WIDTH > WIDTH:
                run = screen_change.lose_screen(game_score)
                if run: 
                    reset()
        elif direction == 1:
            position.x -= VEL
            if position.x - VEL < 0:
                run = screen_change.lose_screen(game_score)
                if run: 
                    reset()
        elif direction == 2:   
            position.y -= VEL
            if position.y - VEL < BORDER_MAX_HEIGHT:
                run = screen_change.lose_screen(game_score)
                if run: 
                    reset()
        elif direction == 3:
            position.y += VEL
            if position.y + VEL > HEIGHT:
                run = screen_change.lose_screen(game_score)
                if run: 
                    reset()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            direction = 0
        elif keys_pressed[pygame.K_LEFT]:
            direction = 1
        elif keys_pressed[pygame.K_UP]:
            direction = 2
        elif keys_pressed[pygame.K_DOWN]:
            direction = 3
        if keys_pressed[pygame.K_s]:
            current_operation = "subtraction"
        elif keys_pressed[pygame.K_a]:
            current_operation = "addition"
        
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert ms to seconds
        if elapsed_time <= 0:
            run = screen_change.lose_screen(game_score)
            if run:
                reset()

        if (target_score == score):
            target_score += random.randint(10, 20)
            VEL_CHASE += 0.25
            VEL += 0.5
            game_score += 10
        elif score > target_score:
            run = screen_change.lose_screen(game_score)
            if run:
                reset()

        draw_window(position, direction, 60 - elapsed_time)

        for chaser in chasers:
            if (chaser.get_rect().collidepoint(position.x + 25, position.y + 25)):
                run = screen_change.lose_screen(game_score)
                if run:
                    reset()

        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()