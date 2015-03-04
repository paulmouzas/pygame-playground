import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((700, 700))

white = (255, 255, 255)
black = (0, 0, 0)


clock = pygame.time.Clock()

running = True

def addVectors((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def draw_spaceship(x, y, angle):
    magnitude = 30
    p1_angle = angle
    p2_angle = angle + math.radians(145)
    p3_angle = angle - math.radians(145)
    p1 = (math.cos(p1_angle) * magnitude + x, -math.sin(p1_angle) * magnitude + y)
    p2 = (math.cos(p2_angle) * magnitude + x, -math.sin(p2_angle) * magnitude + y)
    p3 = (math.cos(p3_angle) * magnitude + x, -math.sin(p3_angle) * magnitude + y)

    pygame.draw.line(screen, white, (p1[0], p1[1]), (p2[0], p2[1]))
    pygame.draw.line(screen, white, (p1[0], p1[1]), (p3[0], p3[1]))
    pygame.draw.line(screen, white, (p2[0], p2[1]), (p3[0], p3[1]))


angle = math.pi / 2
angle_change = 0
trajectory_angle = angle

x, y = 350, 350

speed = 0
thrust = 0
max_speed = 8

stars = [(random.randint(0, 699), random.randint(0, 699)) for x in range(140)]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle_change = .03
            elif event.key == pygame.K_RIGHT:
                angle_change = -.03
            elif event.key == pygame.K_UP:
                thrust = .1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                angle_change = 0
            elif event.key == pygame.K_RIGHT:
                angle_change = 0
            elif event.key == pygame.K_UP:
                thrust = 0


    screen.fill(black)

    for star in stars:
        star_x, star_y = star[0], star[1]
        pygame.draw.line(screen, white, (star_x, star_y), (star_x, star_y))

    angle += angle_change

    trajectory_angle, speed = addVectors((trajectory_angle, speed), (angle,
        thrust))

    if speed > max_speed:
        speed = max_speed
    x += math.cos(trajectory_angle) * speed
    y -= math.sin(trajectory_angle) * speed

    x %= 760
    y %= 760

    draw_spaceship(x, y, angle)

    pygame.display.flip()

    clock.tick(90)

pygame.quit()
