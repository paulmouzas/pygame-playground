import pygame
import random
import math

with open('maze.txt', 'r') as f:
    WIDTH, HEIGHT = [int(x) for x in f.readline().split()]
    maze = []
    for row in range(HEIGHT):
        line = f.readline().strip()
        if 'S' in line:
            start = (row, line.index('S'))
        if 'E' in line:
            end = (row, line.index('E'))
        maze.append(list(line))


BLOCKSIZE = 15

SCREENWIDTH = BLOCKSIZE * WIDTH
SCREENHEIGHT = BLOCKSIZE * HEIGHT


screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (200, 200, 200)
black = (0, 0, 0)



def draw_maze(maze):
    top = 0
    left = 0
    for line in maze:
        for square in line:
            if square == '#':
                pygame.draw.rect(screen, blue, (left, top, BLOCKSIZE, BLOCKSIZE))
            left += BLOCKSIZE
        left = 0
        top += BLOCKSIZE

pygame.init()
clock = pygame.time.Clock()
print maze

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    draw_maze(maze)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
