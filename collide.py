import pygame
import random
import math

pygame.init()
width, height = 700, 700
screen = pygame.display.set_mode((width, height))
drag = 0.999
elasticity = 0.75
gravity = ((math.pi * 3) / 2, 0.2)

white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (200, 200, 200)
black = (0, 0, 0)

def add_vectors((angle1, length1), (angle2, length2)):
    x = math.cos(angle1) * length1 + math.cos(angle2) * length2
    y = math.sin(angle1) * length1 + math.sin(angle2) * length2
    angle = math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p2.x - p2.x

    distance = math.hypot(dx, dy)
    if distance < p1.size + p2.size:
        tangent = math.atan2(dy, dx)
        p1.angle += tangent
        p2.angle += tangent
        p1.speed, p2.speed = p2.speed, p1.speed

class Particle:
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed = 9
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.angle, self.speed = add_vectors((self.angle, self.speed), gravity)
        self.x += math.cos(self.angle) * self.speed
        self.y -= math.sin(self.angle) * self.speed
        self.speed *= drag

    def bounce(self):
        if self.x > width - self.size:
            d = self.x - (width - self.size)
            self.x = (width - self.size) - d
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.x < 0 + self.size:
            d = self.x - self.size
            self.x = self.size -d
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            d = self.y - (height - self.size)
            self.y = (height - self.size) - d
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.y < 0 + self.size:
            d = self.y - self.size
            self.y = self.size - d
            self.angle = - self.angle
            self.speed *= elasticity


clock = pygame.time.Clock()

number_of_particles = 10
my_particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width - size)
    y = random.randint(size, height - size)
    random_particle = Particle((x, y), size)
    random_particle.angle = random.uniform(0, math.pi * 2)
    my_particles.append(random_particle)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)

    for i, p1 in enumerate(my_particles):
        p1.move()
        p1.bounce()
        for p2 in my_particles[i+1:]:
            collide(p1, p2)
        p1.display()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
