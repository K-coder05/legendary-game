import pygame
import main

def lose_screen():
<<<<<<< HEAD
    lose_run = True
    while lose_run:
        main.WIN.fill((0, 0, 0))
        main.draw_text("You lost, better luck next time", main.FONT, (255, 255, 255), 200, 210)
        main.draw_text("Press 'Space' to try again", main.FONT, (255, 255, 255), 235, 260)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    lose_run = False
                    return True
            if event.type == pygame.QUIT:
                lose_run = False
                return False
            
        pygame.display.update()

=======
    main.WIN.fill((0, 0, 0))
    pygame.time.delay(1000)
    main.draw_text("You lost, better luck next time", main.FONT, (255, 255, 255), 350, 300)
    pygame.display.update()

    return False
>>>>>>> a5e5b45ca3be1718da2c1aeb268ee96b8c520728

def main_screen():
    main_run = True
    while main_run:
        main.WIN.fill((0, 0, 0))
<<<<<<< HEAD
        main.draw_text("Welcome to Legendary Game", main.FONT, (255, 255, 255), 220, 210)
        main.draw_text("Press 'Space' to start", main.FONT, (255, 255, 255), 270, 260)
=======
        main.draw_text("Welcome to Legendary Game", main.FONT, (255, 255, 255), 300, 250)
        main.draw_text("Press 'Space' to start", main.FONT, (255, 255, 255), 350, 300)
>>>>>>> a5e5b45ca3be1718da2c1aeb268ee96b8c520728

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_run = False
                    return True
            if event.type == pygame.QUIT:
<<<<<<< HEAD
                main_run = False
=======
>>>>>>> a5e5b45ca3be1718da2c1aeb268ee96b8c520728
                return False
            
        pygame.display.update()


def pause_screen():
    game_paused = True
    while game_paused:
        # Draw the pause screen
        main.WIN.fill((0, 0, 0))
        main.draw_text("Press 'Space' to Resume", main.FONT, (255, 255, 255), 250, 210)
        main.draw_text("Press 'Escape' to exit", main.FONT, (255, 255, 255), 280, 260)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_paused = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = False
                    return True
                if event.key == pygame.K_ESCAPE:
                    game_paused = False
                    main.run = False
    

        pygame.display.update()


def win_screen():
<<<<<<< HEAD
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
        
=======
    main.WIN.fill((0, 0, 0))
    main.draw_text("Congrats, You Won!", main.FONT, (255, 255, 255), 300, 250)
    main.draw_text("Next Level Starting Soon...", main.FONT, (255, 255, 255), 350, 300)
    return True
>>>>>>> a5e5b45ca3be1718da2c1aeb268ee96b8c520728
