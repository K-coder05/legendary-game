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
NUM_OF_GAS_CANS = 4


CLOCK = pygame.time.Clock()

GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

score = 0
position = pygame.Rect(300, 100, MAIN_WIDTH, MAIN_HEIGHT)
position_chase = pygame.Rect(800, 300, MAIN_WIDTH, MAIN_HEIGHT)
gas_spawn = Gas(WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT)
direction = 0 # 0 = right, 1 = left, 2 = up, 3 = down
start_time = pygame.time.get_ticks()

def reset():
    global score, position, position_chase, gas_spawn, direction, start_time
    score = 0
    position = pygame.Rect(300, 100, MAIN_WIDTH, MAIN_HEIGHT)
    position_chase = pygame.Rect(800, 300, MAIN_WIDTH, MAIN_HEIGHT)
    gas_spawn = Gas(WIDTH, HEIGHT, MAIN_WIDTH, MAIN_HEIGHT)
    direction = 0 # 0 = right, 1 = left, 2 = up, 3 = down
    start_time = pygame.time.get_ticks()

def draw_text(text, font, text_color, x_offset, y_offset):
    img = font.render(text, True, text_color)
    img_rect = img.get_rect(center=(WIDTH/2 + x_offset, HEIGHT/2 + y_offset))
    WIN.blit(img, img_rect)

def draw_score(score, font, text_color, x, y):
    score = font.render(str(score), True, text_color)
    WIN.blit(score, (x, y))

def draw_window(position, position_chase, direction, chase_direction, elapsed_time):
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

    elapsed_time = round(elapsed_time, 2)
    timer_text = f"Time: {elapsed_time}s"
    timer_surface = FONT.render(timer_text, True, (255, 255, 255))

    WIN.fill(GRAY)
    WIN.blit(mainSprite, (position.x, position.y))
    WIN.blit(chaserSprite, (position_chase.x, position_chase.y))
    WIN.blit(timer_surface, (800, 50))
    
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
    

    # Tell interpreter to find global variables
    global score, position, position_chase, gas_spawn, direction, start_time  

    run = screen_change.main_screen()

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
                run = screen_change.lose_screen()
                if run: 
                    reset()
        elif direction == 1:
            position.x -= VEL
            if position.x - VEL < 0:
                run = screen_change.lose_screen()
                if run: 
                    reset()
        elif direction == 2:   
            position.y -= VEL
            if position.y - VEL < 0:
                run = screen_change.lose_screen()
                if run: 
                    reset()
        elif direction == 3:
            position.y += VEL
            if position.y + VEL > HEIGHT:
                run = screen_change.lose_screen()
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

        chase_direction = chase_mechanic(position, position_chase)

        if (abs(position.x - position_chase.x) <= MAIN_WIDTH) and (abs(position.y - position_chase.y) <= MAIN_HEIGHT):
            run = screen_change.lose_screen()
            if run:
                reset()


        for gas_spawn in gas_spawns:
            if position.colliderect(gas_spawn.gas_rect):
                score += gas_spawn.random_gas_num
                gas_spawn.respawn()
            
        
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert ms to seconds
        if elapsed_time <= 0:
            run = screen_change.lose_screen()
            if run:
                reset()
        draw_window(position, position_chase, direction, chase_direction, 60 - elapsed_time)
        gas_spawn.draw_gas(WIN)


        draw_score(str(score), FONT, WHITE, 25, 25)
        pygame.display.update()

        if (abs(position.x - position_chase.x) <= MAIN_WIDTH / 2) and (abs(position.y == position_chase.y)):
            run = screen_change.lose_screen()
            if run:
                reset()
        
        

    pygame.quit()



if __name__ == "__main__":
    main()