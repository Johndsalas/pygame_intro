''' File for pygame introduction'''

import pygame
import os

WIDTH, HIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HIGHT))

# RGB red green blue 0-255
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER =pygame.Rect(WIDTH//2 - 5, 0, 10, HIGHT)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2 

VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HIGHT = 55, 40

# load spaceship images then scale and rotate them
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, 
                                                                 (SPACESHIP_WIDTH, SPACESHIP_HIGHT)),
                                                                 270)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, 
                                                              (SPACESHIP_WIDTH, SPACESHIP_HIGHT)),
                                                              90)

# window title
pygame.display.set_caption("First Caption")

def draw_window(yellow, red, yellow_bullets, red_bullets):

    WIN.fill(WHITE)

    pygame.draw.rect(WIN, BLACK, BORDER)

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    ''' handels yellow ship's movements and keeps yellow ship in bounds'''

    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # left
            yellow.x -= VEL

    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # right
        yellow.x += VEL

    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HIGHT:  # down
        yellow.y += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # up
        yellow.y -= VEL

def red_handle_movement(keys_pressed, red):
    ''' handels red ship's movements and keeps red ship in bounds'''
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # left
        red.x -= VEL

    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # right
       red.x += VEL

    if keys_pressed[pygame.K_DOWN] and red.y - VEL + red.height < HIGHT - 15: # down
        red.y += VEL

    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # up
        red.y -= VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):

    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            yellow_bullets.remove(bullet)

def main():

    # create object Rect(x,y,hight,with)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            
            # quits game if close box is clicked
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # fire bullets
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_e and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                # if event.key == pygame.K_QUESTION and len(red_bullets) < MAX_BULLETS:
                #     bullet = pygame.Rect
                #     red_bullets.append(bullet)

        # gets keys that are pressed and responds to those keys
        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # draws the board (Takes in created objects to draw at new coordenants)
        draw_window(red, yellow, red_bullets, yellow_bullets)




if __name__ == "__main__":
    main()
