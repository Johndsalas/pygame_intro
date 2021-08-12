''' File for pygame introduction'''

import pygame
import os

WIDTH, HIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HIGHT))

# RGB red green blue 0-255
WHITE = (255,255,255)

# set Frames Per Second
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HIGHT))


RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HIGHT))

VEL = 5

# window title
pygame.display.set_caption("First Caption")

def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):

    if keys_pressed[pygame.K_a]: # left
            yellow.x -= VEL

    if keys_pressed[pygame.K_d]: # right
        yellow.x += VEL

    if keys_pressed[pygame.K_s]: # down
        yellow.y += VEL

    if keys_pressed[pygame.K_w]: # up
        yellow.y -= VEL


def main():

    # create object Rect(x,y,hight,with)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HIGHT)

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # gets keys that are pressed and responds to those keys
        keys_pressed = pygame.key.get_pressed()

        

        # draws the board (Takes in created objects to draw at new coordenants)       
        draw_window(red, yellow)
    
        
    pygame.quit()

if __name__ == "__main__":
    main()
