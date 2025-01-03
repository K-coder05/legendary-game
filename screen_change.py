import button
import pygame
from pygame import mixer
import main

# Load music
mixer.init()

# Load button images
play_img = pygame.image.load("Assets/MenuButtons/PlayButton.png").convert_alpha()
pause_img = pygame.image.load("Assets/MenuButtons/PauseButton.png").convert_alpha()
quit_img = pygame.image.load("Assets/MenuButtons/QuitButton.png").convert_alpha()


def controls_screen():
    # Load control images
    key_left_img = pygame.image.load("Assets/MenuButtons/KeyboardLeft.png").convert_alpha()
    key_left_pushed_img = pygame.image.load("Assets/MenuButtons/KeyboardLeftPushed.png").convert_alpha()
    key_right_img = pygame.image.load("Assets/MenuButtons/KeyboardRight.png").convert_alpha()
    key_right_pushed_img = pygame.image.load("Assets/MenuButtons/KeyboardRightPushed.png").convert_alpha()
    key_up_img = pygame.image.load("Assets/MenuButtons/KeyboardUp.png").convert_alpha()
    key_up_pushed_img = pygame.image.load("Assets/MenuButtons/KeyboardUpPushed.png").convert_alpha()
    key_down_img = pygame.image.load("Assets/MenuButtons/KeyboardDown.png").convert_alpha()
    key_down_pushed_img = pygame.image.load("Assets/MenuButtons/KeyboardDownPushed.png").convert_alpha()
    key_space1_img = pygame.image.load("Assets/MenuButtons/KeyboardSpace1.png").convert_alpha()
    key_space2_img = pygame.image.load("Assets/MenuButtons/KeyboardSpace2.png").convert_alpha()
    key_space3_img = pygame.image.load("Assets/MenuButtons/KeyboardSpace3.png").convert_alpha()
    key_add_image = pygame.image.load("Assets/MenuButtons/KeyboardA.png").convert_alpha()
    key_add_pushed_image = pygame.image.load("Assets/MenuButtons/KeyboardAPushed.png").convert_alpha()
    key_sub_image = pygame.image.load("Assets/MenuButtons/KeyboardS.png").convert_alpha()
    key_sub_pushed_image = pygame.image.load("Assets/MenuButtons/KeyboardSPushed.png").convert_alpha()

    # 1100 x 700 (550 x 350) window dimensions
    left_pushed = right_pushed = up_pushed = down_pushed = a_pushed = s_pushed = False

    controls_run = True
    while controls_run:
        main.WIN.fill((0, 0, 0))

        main.draw_text("CONTROLS", main.FONT, (255, 255, 255), 0, -250)
        main.draw_text("________", main.FONT, (255, 255, 255), 0, -250)

        main.draw_text("Use the arrow keys to move", main.FONT, (255, 255, 255), 0, -200)
        if (not left_pushed):
            main.WIN.blit(key_left_img, (main.WIDTH/2 - 100, main.HEIGHT/2 - 150))
        else:
            main.WIN.blit(key_left_pushed_img, (main.WIDTH/2 - 100, main.HEIGHT/2 - 150))
        if (not right_pushed):
            main.WIN.blit(key_right_img, (main.WIDTH/2 - 50, main.HEIGHT/2 - 150))
        else:
            main.WIN.blit(key_right_pushed_img, (main.WIDTH/2 - 50, main.HEIGHT/2 - 150))
        if (not up_pushed):
            main.WIN.blit(key_up_img, (main.WIDTH/2 + 18, main.HEIGHT/2 - 150))
        else:
            main.WIN.blit(key_up_pushed_img, (main.WIDTH/2 + 18, main.HEIGHT/2 - 150))
        if (not down_pushed):
            main.WIN.blit(key_down_img, (main.WIDTH/2 + 68, main.HEIGHT/2 - 150))
        else:
            main.WIN.blit(key_down_pushed_img, (main.WIDTH/2 + 68, main.HEIGHT/2 - 150))

        main.draw_text("Press 'Space' to pause the game", main.FONT, (255, 255, 255), 0, -50)
        main.WIN.blit(key_space1_img, (main.WIDTH/2 - 48, main.HEIGHT/2))
        main.WIN.blit(key_space2_img, (main.WIDTH/2 - 16, main.HEIGHT/2))
        main.WIN.blit(key_space3_img, (main.WIDTH/2 + 15, main.HEIGHT/2))

        main.draw_text("Press 'A' to go into add mode", main.FONT, (255, 255, 255), -15, 100)
        if (not a_pushed):
            main.WIN.blit(key_add_image, (main.WIDTH/2 - 330, main.HEIGHT/2 + 80))
        else:
            main.WIN.blit(key_add_pushed_image, (main.WIDTH/2 - 330, main.HEIGHT/2 + 80))

        main.draw_text("Press 'S' to go into subtract mode", main.FONT, (255, 255, 255), 30, 200)
        if (not s_pushed):
            main.WIN.blit(key_sub_image, (main.WIDTH/2 - 330, main.HEIGHT/2 + 180))
        else:
            main.WIN.blit(key_sub_pushed_image, (main.WIDTH/2 - 330, main.HEIGHT/2 + 180))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_pushed = True
                if event.key == pygame.K_RIGHT:
                    right_pushed = True
                if event.key == pygame.K_DOWN:
                    down_pushed = True
                if event.key == pygame.K_UP:
                    up_pushed = True
                if event.key == pygame.K_a:
                    a_pushed = True
                if event.key == pygame.K_s:
                    s_pushed = True
                if event.key == pygame.K_SPACE:
                    controls_run = True
                    mixer.music.stop()
                    mixer.music.load("Assets/Sounds/Music/ChillMusic.mp3")
                    mixer.music.play()
                    return True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_pushed = False
                if event.key == pygame.K_RIGHT:
                    right_pushed = False
                if event.key == pygame.K_DOWN:
                    down_pushed = False
                if event.key == pygame.K_UP:
                    up_pushed = False
                if event.key == pygame.K_a:
                    a_pushed = False
                if event.key == pygame.K_s:
                    s_pushed = False
            if event.type == pygame.QUIT:
                controls_run = False
                return False


        pygame.display.update()


def lose_screen(game_score):

    play_button = button.Button(main.WIDTH/2 - 80, main.HEIGHT/2 + 50, play_img, 1.5)
    quit_button = button.Button(main.WIDTH/2 - 75, main.HEIGHT/2 + 150, quit_img, 1.5)

    mixer.music.stop()
    mixer.music.load("Assets/Sounds/Explosion.wav")
    mixer.music.play()
    
    lose_run = True
    while lose_run:
        main.WIN.fill((0, 0, 0))

        losing_message = "You lost! Score: " + str(game_score)
        main.draw_text(losing_message, main.FONT, (255, 255, 255), 0, -100)
        
        if play_button.draw(main.WIN):
            lose_run = False
            mixer.music.load("Assets/Sounds/Music/ChillMusic.mp3")
            mixer.music.play(loops=8)
            return True
        if quit_button.draw(main.WIN):
            lose_run = False
            return False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose_run = False
                return False
            
        pygame.display.update()


def main_screen():
    play_button = button.Button(main.WIDTH / 2 - 80, main.HEIGHT / 2 - 50, play_img, 1.5)
    quit_button = button.Button(main.WIDTH / 2 - 75, main.HEIGHT / 2 + 50, quit_img, 1.5)
    
    background_image = pygame.image.load("Assets/MenuButtons/MenuBackground.jpg")
    background_image = pygame.transform.scale(background_image, (main.WIDTH, main.HEIGHT))

    mixer.music.load("Assets/Sounds/Music/RelaxedSpaceMusic.mp3")
    mixer.music.play(loops=100)
    
    main_run = True
    while main_run:
        main.WIN.blit(background_image, (0,0))
        main.draw_text("Welcome to Velocity Math", main.FONT, (0, 0, 0), 0, -100)
        
        if play_button.draw(main.WIN):
            main_run = False
            return True
        if quit_button.draw(main.WIN):
            main_run = False
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_run = False
                return False
            
        pygame.display.update()


def pause_screen():
    pause_button = button.Button(main.WIDTH/2 - 80, main.HEIGHT/2 + 50, pause_img, 1.5)
    quit_button = button.Button(main.WIDTH/2 - 75, main.HEIGHT/2 + 150, quit_img, 1.5)
    game_paused = True
    while game_paused:
        # Draw the pause screen
        main.WIN.fill((192,192,192))
        main.draw_text("Game paused.", main.FONT, (0, 0, 0), 0, -100)
        
        if pause_button.draw(main.WIN):
            game_paused = False
            return True
        if quit_button.draw(main.WIN):
            game_paused = False
            return False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_paused = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = True
                    return True

        pygame.display.update()


def win_screen():
    win_run = True
    while win_run:
        main.WIN.fill((0, 0, 0))
        main.draw_text("Congratuations!", main.FONT, (255, 255, 255), 200, 210)
        main.draw_text("Press 'Space' to try again", main.FONT, (255, 255, 255), 150, 260)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    win_run = False
                    return True
            if event.type == pygame.QUIT:
                win_run = False
                return False
            
        pygame.display.update()
        
