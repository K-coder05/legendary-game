import pygame
import os
import screen_change
from Gas import Gas 

pygame.init()

# Initialize the game
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Legendary Game")

# Define variables
FPS = 60
VEL = 5
VEL_CHASE = 1
MAIN_WIDTH, MAIN_HEIGHT = 55, 40 # Size of Sprites
FONT = pygame.font.SysFont("Arial", 32)

LEBRON_IMAGE = pygame.image.load(os.path.join('Assets', 'lebron.png'))
LEBRON = pygame.transform.scale(LEBRON_IMAGE, (MAIN_WIDTH, MAIN_HEIGHT))
BRONNY_IMAGE = pygame.image.load(os.path.join('Assets', 'bronny.png'))
BRONNY = pygame.transform.scale(BRONNY_IMAGE, (MAIN_WIDTH, MAIN_HEIGHT))

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    WIN.blit(img, (x, y))

def draw_window(position, position_chase):
    WIN.fill((255, 255, 255))
    WIN.blit(LEBRON, (position.x, position.y))
    WIN.blit(BRONNY, (position_chase.x, position_chase.y))
    
    pygame.display.update()

def chase_mechanic(position, position_chase):
    distance_x = abs(position.x - position_chase.x)
    distance_y = abs(position.y - position_chase.y)

    if distance_x > distance_y:
        if (position.x < position_chase.x):
            position_chase.x -= VEL_CHASE
        else:
            position_chase.x += VEL_CHASE
    else:
        if (position.y < position_chase.y):
            position_chase.y -= VEL_CHASE
        else:
            position_chase.y += VEL_CHASE


def main():
    position = pygame.Rect(300, 100, MAIN_WIDTH, MAIN_HEIGHT)
    position_chase = pygame.Rect(800, 300, MAIN_WIDTH, MAIN_HEIGHT)
    gas_spawn = Gas(WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT)
    direction = 0 # 0 = right, 1 = left, 2 = up, 3 = down

    run = screen_change.main_screen()

    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Define the movement of the character
        if direction == 0:
            position.x += VEL
            if position.x + VEL + MAIN_WIDTH > WIDTH:
                direction = 1
        elif direction == 1:
            position.x -= VEL
            if position.x - VEL < 0:
                direction = 0
        elif direction == 2:   
            position.y -= VEL
            if position.y - VEL < 0:
                direction = 3
        elif direction == 3:
            position.y += VEL
            if position.y + VEL > HEIGHT:
                direction = 2

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            direction = 0
        elif keys_pressed[pygame.K_LEFT]:
            direction = 1
        elif keys_pressed[pygame.K_UP]:
            direction = 2
        elif keys_pressed[pygame.K_DOWN]:
            direction = 3

        chase_mechanic(position, position_chase)

        if position.colliderect(gas_spawn.gas_rect):
            gas_spawn.respawn()
            
        draw_window(position, position_chase)
        gas_spawn.draw_gas(WIN)
        pygame.display.update()

        if (abs(position.x - position_chase.x) <= MAIN_WIDTH / 1.5) and (abs(position.y - position_chase.y) <= MAIN_HEIGHT / 1.5):
            run = screen_change.lose_screen()
            print("You lose!")
        


    pygame.quit()



if __name__ == "__main__":
    main()