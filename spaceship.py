import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((700, 700))

white   = (255, 255, 255)
black   = (000, 000, 000)
red     = (255, 000, 000)

clock = pygame.time.Clock()

circle = pygame.Surface((30, 30,))

running = True

def bullet_hit_asteroid(asteroid, bullet):
    # asteroid  => (x, y, r)
    # bullet    => (angle, x, y)
    a_x, a_y, a_r, _, _ = asteroid

    b_a, b_x, b_y = bullet

    dx = a_x - b_x
    dy = a_y - b_y

    distance = math.hypot(dx, dy)
    if distance < a_r:
        return True
    return False

def addVectors((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def draw_asteroid(a):
    a[0] %= 760
    a[1] %= 760
    pygame.draw.circle(screen, white, (int(a[0]), int(a[1])), a[2], 1)

def explode_asteroid(a):
    # this function will take the position and radius of an asteroid and return
    # the points and radii of three smaller asteroids

    x, y, r, angle, speed = a

    # this will be how far away from the center the exploded asteroids will be
    diff = r * 1.3
    # make the new size for the asteroids half as big
    new_r = r / 2

    # set a random angle and speed
    angle_1 = random.random() * (math.pi * 2)
    speed_1 = random.random() * .5

    angle_2 = random.random() * (math.pi * 2)
    speed_2 = random.random() * .5

    angle_3 = random.random() * (math.pi * 2)
    speed_3 = random.random() * .5

    x1, y1 = int(math.cos(angle_1) * diff + x), int(math.sin(angle_1) * diff + y)
    x2, y2 = int(math.cos(angle_2) * diff + x), int(math.sin(angle_2) * diff + y)
    x3, y3 = int(math.cos(angle_3) * diff + x), int(math.sin(angle_3) * diff + y)

    return [x1, y1, new_r, angle_1, speed_1], [x2, y2, new_r, angle_2, speed_2], [x3, y3, new_r, angle_3, speed_3]
    

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
max_speed = 12

asteroids = []

# asteroid -> (x, y, raidus, angle, speed)
asteroid = [100, 100, 40, math.pi * 6 / 11, .5]
asteroid2 = [500, 400, 60, math.pi * 3 / 2, .2]
asteroids.append(asteroid)
asteroids.append(asteroid2)

stars = [(random.randint(0, 699), random.randint(0, 699)) for x in range(140)]

bullet_speed = 5

bullets = []

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
                thrust = .04
            elif event.key == pygame.K_SPACE:
                bullet_angle = angle
                # adjust the position of the bullet so that it is comming
                # from the front point of the ship
                offset_bullet_x = x + math.cos(bullet_angle) * 30
                offset_bullet_y = y + -math.sin(bullet_angle) * 30
                bullets.append([bullet_angle, offset_bullet_x, offset_bullet_y])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                angle_change = 0
            elif event.key == pygame.K_RIGHT:
                angle_change = 0
            elif event.key == pygame.K_UP:
                thrust = 0

    screen.fill(black)

    # draw the bullets
    for b in bullets:
        bullet_angle = b[0]
        bullet_x = b[1]
        bullet_y = b[2]
        bullet_x_offset = math.cos(bullet_angle) * 4
        bullet_y_offset = -math.sin(bullet_angle) * 4

        pygame.draw.line(screen,
                (255, 0, 0),
                (bullet_x, bullet_y),
                (int(bullet_x + bullet_x_offset), int(bullet_y + bullet_y_offset)),
                2
            )

        b[1] += math.cos(bullet_angle) * bullet_speed
        b[2] -= math.sin(bullet_angle) * bullet_speed
        if b[1] > 700 or b[2] > 700 or b[1] < 0 or b[2] < 0:
            bullets.remove(b)

    # draw the stars
    for star in stars:
        star_x, star_y = star[0], star[1]
        pygame.draw.line(screen, white, (star_x, star_y), (star_x, star_y))


    # this is the direction the spaceship is pointing
    angle += angle_change

    # the trajectory angle is the angle that the spaceship is moving, not the
    # angle it is pointing. if the player is pressing the up key, a vector
    # will be added to change the direciton and speed 
    trajectory_angle, speed = addVectors((trajectory_angle, speed),
                                            (angle, thrust))

    # this just limits the speed of the spaceship
    if speed > max_speed:
        speed = max_speed

    # update the position of the spaceship
    x += math.cos(trajectory_angle) * speed
    y -= math.sin(trajectory_angle) * speed

    # make the spaceship appear on the other side of the it goes beyond the
    # screen

    # make the spaceship appear on the other side if it goes beyond the screen
    x %= 760
    y %= 760

    for a in asteroids:
        # asteroid -> [x, y, r, angle, speed]


        # update the positions of the asteroids
        a[0] += math.cos(a[3]) * a[4]
        a[1] -= math.sin(a[3]) * a[4]

        draw_asteroid(a)


    # check for bullets hitting asteroid
    asteroids_copy = asteroids[:]
    bullets_copy = bullets[:]
    for b in bullets:
        for a in asteroids:
            if bullet_hit_asteroid(a, b):
                # remove all asteroids smaller than 10
                if a[2] < 20:
                    asteroids_copy.remove(a)
                    continue
                a1, a2, a3 = explode_asteroid(a)

                asteroids_copy.remove(a)
                bullets_copy.remove(b)

                asteroids_copy.append(a1)
                asteroids_copy.append(a2)
                asteroids_copy.append(a3)

    asteroids = asteroids_copy[:]
    bullets = bullets_copy[:]

    draw_spaceship(x, y, angle)

    pygame.display.flip()

    clock.tick(90)

pygame.quit()
