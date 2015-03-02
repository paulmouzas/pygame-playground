import pygame
import math

pygame.init()
screen = pygame.display.set_mode((700, 700))

white = (255, 255, 255)
black = (0, 0, 0)

x = 350
y = 350
radius = 10
speed = 0
drag = .999
angle = 0


clock = pygame.time.Clock()


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


    if click_down:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - x
        dy = mouse_y - y
        angle = math.atan2(dx, dy) + (math.pi / 2)
        speed = math.hypot(dx, dy) * .04
        pygame.draw.line(screen, white, (mouse_x, mouse_y), (x, y))
    else:
        x += math.cos(angle) * speed
        y -= math.sin(angle) * speed


    if x > 690:
        # setting the x or y ensures that the particle doesn't 'stick' to the boundaries
        x = 690
        angle = math.pi-angle
    elif x < 10:
        x = 10
        angle = math.pi-angle
    if y > 690:
        y = 690
        angle = -angle
    elif y < 10:
        y = 10
        angle = -angle
    pygame.display.flip()
    clock.tick(90)

pygame.quit()