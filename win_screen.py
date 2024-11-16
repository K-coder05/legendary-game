import pygame
import main_screen

def win_screen():
    main_screen.screen.fill((0, 0, 0))
    main_screen.draw_text("Congratuations!", main_screen.font, main_screen.text_color, 200, 250)

    pygame.time.delay(10000)

