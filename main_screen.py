import pygame

pygame.init()

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Legendary Game")

font = pygame.font.SysFont("times new roman", 30)
text_color = (255, 255, 255)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

run = True
while run:
    screen.fill((0, 0, 0))
    draw_text("Welcome to Legendary Game", font, text_color, 200, 250)
    draw_text("Press 'Space' to start", font, text_color, 250, 300)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space") #we can put the main game loop here
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.update()
    
pygame.quit()