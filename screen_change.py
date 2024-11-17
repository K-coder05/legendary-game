import pygame
import main

def lose_screen():
    main.WIN.fill((0, 0, 0))
    pygame.time.delay(1000)
    main.draw_text("You lost, better luck next time", main.FONT, (255, 255, 255), 350, 300)
    pygame.display.update()

    return False

def main_screen():
    run = True
    while run:
        main.WIN.fill((0, 0, 0))
        main.draw_text("Welcome to Legendary Game", main.FONT, (255, 255, 255), 300, 250)
        main.draw_text("Press 'Space' to start", main.FONT, (255, 255, 255), 350, 300)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
            if event.type == pygame.QUIT:
                return False
            
        pygame.display.update()

def win_screen():
    main.WIN.fill((0, 0, 0))
    main.draw_text("Congrats, You Won!", main.FONT, (255, 255, 255), 300, 250)
    main.draw_text("Next Level Starting Soon...", main.FONT, (255, 255, 255), 350, 300)
    return True