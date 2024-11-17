import pygame
import os
import screen_change
from Gas import Gas 

pygame.init()

# Initialize the game
WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Legendary Game")

# Define variables
FPS = 60
VEL = 5
VEL_CHASE = 1
MAIN_WIDTH, MAIN_HEIGHT = 80, 60
FONT = pygame.font.SysFont("Arial", 32)

GRAY = (128, 128, 128)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    WIN.blit(img, (x, y))

def draw_window(position, position_chase, direction, chase_direction):
   # Load images
    if chase_direction == 0:
        chaser_image = pygame.image.load(os.path.join('Assets/ChaserSprite', 'police_east.png'))
    elif chase_direction == 1:
        chaser_image = pygame.image.load(os.path.join('Assets/ChaserSprite', 'police_west.png'))
    elif chase_direction == 2:
        chaser_image = pygame.image.load(os.path.join('Assets/ChaserSprite', 'police_north.png'))
    else:
        chaser_image = pygame.image.load(os.path.join('Assets/ChaserSprite', 'police_south.png'))

    if direction == 0:
        car_image = pygame.image.load(os.path.join('Assets/CarSprite', 'car_east.png'))
    elif direction == 1:
        car_image = pygame.image.load(os.path.join('Assets/CarSprite', 'car_west.png'))
    elif direction == 2:
        car_image = pygame.image.load(os.path.join('Assets/CarSprite', 'car_north.png'))
    else:
        car_image = pygame.image.load(os.path.join('Assets/CarSprite', 'car_south.png'))

    mainSprite = pygame.transform.scale(car_image, (MAIN_WIDTH, MAIN_HEIGHT))
    chaserSprite = pygame.transform.scale(chaser_image, (MAIN_WIDTH, MAIN_HEIGHT))
   
    WIN.fill(GRAY)
    WIN.blit(mainSprite, (position.x, position.y))
    WIN.blit(chaserSprite, (position_chase.x, position_chase.y))
    
    pygame.display.update()

def chase_mechanic(position, position_chase):
    distance_x = abs(position.x - position_chase.x)
    distance_y = abs(position.y - position_chase.y)

    if distance_x > distance_y:
        if (position.x < position_chase.x):
            position_chase.x -= VEL_CHASE
            return 1
        else:
            position_chase.x += VEL_CHASE
            return 0
    else:
        if (position.y < position_chase.y):
            position_chase.y -= VEL_CHASE
            return 3
        else:
            position_chase.y += VEL_CHASE
            return 2


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = screen_change.pause_screen()

        # Define the movement of the character
        if direction == 0:
            position.x += VEL
            if position.x + VEL + MAIN_WIDTH > WIDTH:
                run = screen_change.lose_screen()
        elif direction == 1:
            position.x -= VEL
            if position.x - VEL < 0:
                run = screen_change.lose_screen()
        elif direction == 2:   
            position.y -= VEL
            if position.y - VEL < 0:
                run = screen_change.lose_screen()
        elif direction == 3:
            position.y += VEL
            if position.y + VEL > HEIGHT:
                run = screen_change.lose_screen()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            direction = 0
        elif keys_pressed[pygame.K_LEFT]:
            direction = 1
        elif keys_pressed[pygame.K_UP]:
            direction = 2
        elif keys_pressed[pygame.K_DOWN]:
            direction = 3

        chase_direction = chase_mechanic(position, position_chase)
        draw_window(position, position_chase, direction, chase_direction)
        chase_mechanic(position, position_chase)

        if (abs(position.x - position_chase.x) <= MAIN_WIDTH) and (abs(position.y - position_chase.y) <= MAIN_HEIGHT):
            run = screen_change.lose_screen()
            if run:
                position = pygame.Rect(300, 100, MAIN_WIDTH, MAIN_HEIGHT)
                position_chase = pygame.Rect(800, 300, MAIN_WIDTH, MAIN_HEIGHT)

        if position.colliderect(gas_spawn.gas_rect):
            gas_spawn.respawn()
            
        draw_window(position, position_chase, direction, chase_direction)
        gas_spawn.draw_gas(WIN)
        pygame.display.update()

        if (abs(position.x - position_chase.x) <= MAIN_WIDTH / 1.75) and (abs(position.y - position_chase.y) <= MAIN_HEIGHT / 1.75):
            run = screen_change.lose_screen()
            print("You lose!")
        
        

    pygame.quit()



if __name__ == "__main__":
    main()