import pygame
import math

pygame.init()
font = pygame.font.SysFont("Arial", 14)

screen = pygame.display.set_mode((700, 700))

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

center = (350, 350)
radius = 300
angle = 0

clock = pygame.time.Clock()

while True:
    screen.fill(black)

    sin = math.sin(angle)
    cos = math.cos(angle)
    tan = math.tan(angle)

    # calculate the x and y coordinate
    y = -radius * sin + 350
    x = radius * cos + 350

    sin_text = font.render('sin: ' + '{0:.2f}'.format(sin), True, (0,128,0))
    cos_text = font.render('cos: ' + '{0:.2f}'.format(cos), True, (0,128,0))
    tan_text = font.render('tan: ' + '{0:.2f}'.format(tan), True, (0,128,0))
    degree_text = font.render('angle: ' + str(int(math.degrees(angle))) + u"\u00b0", True, (0,128,0))

    opposite_x = x
    opposite_y = 350

    adjacent_x = x
    adjacent_y = 350

    # draw the circle
    pygame.draw.circle(screen, white, center, radius, 3) 

    #draw the line from the center to the x and y coordinates
    pygame.draw.line(screen, white, center, (x,y), 3)

    # draw the opposite line
    pygame.draw.line(screen, red, (opposite_x, opposite_y), (x, y), 3)

    # draw the adjacent line
    pygame.draw.line(screen, green, center, (adjacent_x, adjacent_y), 3)

    screen.blit(sin_text, (50, 10))
    screen.blit(cos_text, (50, 30))
    screen.blit(tan_text, (50, 50))
    screen.blit(degree_text, (50, 70))

    pygame.display.flip()

    # reset angle if full sweep completed
    if angle > math.pi * 2:
        angle = 0
    # increase angle by .1 radians
    angle += .01
    clock.tick(50)