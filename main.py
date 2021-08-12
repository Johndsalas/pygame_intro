''' File for pygame introduction'''

import pygame
import os

WIDTH, HIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HIGHT))

# RGB red green blue 0-255
RED = (255,0,0)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

# YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HIGHT))


# RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
# RED_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HIGHT))

# window title
pygame.display.set_caption("First Caption")

# def draw_window():
#     WIN.fill(RED)
#     WIN.blit(YELLOW_SPACESHIP_IMAGE, (300,100))
#     pygame.display.update()

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        WIN.fill(RED)
        pygame.display.update()
    
    
    pygame.quit()

if __name__ == "__main__":
    main()
