import pygame
import math

pygame.init()
screen = pygame.display.set_mode((700, 700))

white = (255, 255, 255)
black = (0, 0, 0)

x = 100
y = 450
radius = 10
speed = 3
drag = .999
angle = math.radians(270)

gravity = (math.pi, 0.02)

clock = pygame.time.Clock()

def addVectors((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

running = True
click_down = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            click_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            click_down = False

    screen.fill(black)
    pygame.draw.circle(screen, white, (int(x), int(y)), radius)
    pygame.display.flip()

    angle, speed = addVectors((angle, speed), gravity)

    if click_down:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - x
        dy = mouse_y - y
        angle = 0.5 * math.pi + math.atan2(dy, dx)
        speed = math.hypot(dx, dy) * .1

    x += math.sin(angle) * speed
    y -= math.cos(angle) * speed

    if x > 690:
        # setting the x or y ensures that the particle doesn't 'stick' to the boundaries
        x = 690
        angle = -angle
    elif x < 10:
        x = 10
        angle = -angle
    if y > 690:
        y = 690
        angle = math.pi - angle
    elif y < 10:
        y = 10
        angle = math.pi - angle

    speed *= drag
    clock.tick(90)

pygame.quit()