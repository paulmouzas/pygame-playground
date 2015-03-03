import pygame
import math

pygame.init()
screen = pygame.display.set_mode((700, 700))

white = (255, 255, 255)
black = (0, 0, 0)


clock = pygame.time.Clock()

running = True

def draw_spaceship(x, y, angle):
    magnitude = 30
    p1_angle = math.radians(angle)
    p2_angle = math.radians(angle) + math.radians(145)
    p3_angle = math.radians(angle) - math.radians(145)
    p1 = (math.cos(p1_angle) * magnitude + x, -math.sin(p1_angle) * magnitude + y)
    p2 = (math.cos(p2_angle) * magnitude + x, -math.sin(p2_angle) * magnitude + y)
    p3 = (math.cos(p3_angle) * magnitude + x, -math.sin(p3_angle) * magnitude + y)

    pygame.draw.polygon(screen, white, [p1, p2, p3]) 

angle = 90
angle_change = 0

x, y = 350, 350

speed = 1

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle_change = 2
            elif event.key == pygame.K_RIGHT:
                angle_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                angle_change = 0
            elif event.key == pygame.K_RIGHT:
                angle_change = 0


    screen.fill(black)

    angle += angle_change
    x += math.cos(math.radians(angle)) * speed
    y -= math.sin(math.radians(angle)) * speed

    draw_spaceship(x, y, angle)

    pygame.display.flip()

    clock.tick(90)

pygame.quit()
