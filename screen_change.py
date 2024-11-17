import button
import pygame
import main


play_img = pygame.image.load("Assets/MenuButtons/PlayButton.png").convert_alpha()
pause_img = pygame.image.load("Assets/MenuButtons/PauseButton.png").convert_alpha()
quit_img = pygame.image.load("Assets/MenuButtons/QuitButton.png").convert_alpha()
    

def controls_screen():
    # Load control images
    key_left_img = pygame.image.load("Assets/MenuButtons/KeyboardLeft.png").convert_alpha()
    key_right_img = pygame.image.load("Assets/MenuButtons/KeyboardRight.png").convert_alpha()
    key_up_img = pygame.image.load("Assets/MenuButtons/KeyboardUp.png").convert_alpha()
    key_down_img = pygame.image.load("Assets/MenuButtons/KeyboardDown.png").convert_alpha()
    key_space1_img = pygame.image.load("Assets/MenuButtons/KeyboardSpace1.png").convert_alpha()
    key_space2_img = pygame.image.load("Assets/MenuButtons/KeyboardSpace2.png").convert_alpha()
    key_space3_img = pygame.image.load("Assets/MenuButtons/KeyboardSpace3.png").convert_alpha()
    key_add_image = pygame.image.load("Assets/MenuButtons/KeyboardA.png").convert_alpha()
    key_sub_image = pygame.image.load("Assets/MenuButtons/KeyboardS.png").convert_alpha()

    # 1100 x 700 (550 x 350) window dimensions

    controls_run = True
    while controls_run:
        main.WIN.fill((0, 0, 0))

        main.draw_text("CONTROLS", main.FONT, (255, 255, 255), 0, -200)

        main.draw_text("Use the arrow keys to move", main.FONT, (255, 255, 255), 0, -100)
        main.WIN.blit(key_left_img, (main.WIDTH/2 - 100, main.HEIGHT/2 - 50))
        main.WIN.blit(key_right_img, (main.WIDTH/2 - 50, main.HEIGHT/2 - 50))
        main.WIN.blit(key_up_img, (main.WIDTH/2 + 18, main.HEIGHT/2 - 50))
        main.WIN.blit(key_down_img, (main.WIDTH/2 + 68, main.HEIGHT/2 - 50))

        main.draw_text("Press 'Space' to pause the game", main.FONT, (255, 255, 255), 0, 50)
        main.WIN.blit(key_space1_img, (main.WIDTH/2 - 48, main.HEIGHT/2 + 100))
        main.WIN.blit(key_space2_img, (main.WIDTH/2 - 15, main.HEIGHT/2 + 100))
        main.WIN.blit(key_space3_img, (main.WIDTH/2 + 16, main.HEIGHT/2 + 100))

        main.draw_text("Press 'A' to go into add mode", main.FONT, (255, 255, 255), 0, 150)
        


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controls_run = True
                    return True
            if event.type == pygame.QUIT:
                controls_run = False
                return False


        pygame.display.update()


def lose_screen():
    play_button = button.Button(main.WIDTH/2 - 80, main.HEIGHT/2 + 50, play_img, 1.5)
    quit_button = button.Button(main.WIDTH/2 - 75, main.HEIGHT/2 + 150, quit_img, 1.5)
    
    lose_run = True
    while lose_run:
        main.WIN.fill((192,192,192))
        
        losing_message = "You lost! Score: " + str(main.score)
        main.draw_text(losing_message, main.FONT, (0, 0, 0), 0, -100)
        
        if play_button.draw(main.WIN):
            lose_run = False
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
    play_button = button.Button(main.WIDTH/2 - 80, main.HEIGHT/2 - 50, play_img, 1.5)
    quit_button = button.Button(main.WIDTH/2 - 75, main.HEIGHT/2 + 50, quit_img, 1.5)
    
    background_image = pygame.image.load("Assets/MenuButtons/MenuBackground.jpg")
    background_image = pygame.transform.scale(background_image, (main.WIDTH, main.HEIGHT))
    
    main_run = True
    while main_run:
        main.WIN.blit(background_image, (0,0))
        main.draw_text("Welcome to Legendary Game", main.FONT, (0, 0, 0), 0, -100)
        
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
        
