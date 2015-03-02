import pygame
import math

pygame.init()
font = pygame.font.SysFont("Arial", 14)

screen = pygame.display.set_mode((700, 700))

white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

angle = 0
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    y = math.sin(angle) * 70 + 350
    pygame.draw.line(screen, white, (x, y), (x, y), 3)
    pygame.display.flip()
    x += 1
    angle += .1
    if x > 700:
        x = 0
        screen.fill(black)
    clock.tick(50)
pygame.quit()