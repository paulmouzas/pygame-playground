import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((700, 700))

white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (200, 200, 200)
black = (0, 0, 0)

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
