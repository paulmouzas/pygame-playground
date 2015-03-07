import pygame
import random
import math

with open('maze.txt', 'r') as f:
    WIDTH, HEIGHT = [int(x) for x in f.readline().split()]
    tmp_maze = []
    for row in range(HEIGHT):
        line = f.readline().strip()
        if 'S' in line:
            start = (row, line.index('S'))
        tmp_maze.append(list(line))

maze_copy = tmp_maze[:]

maze = maze_copy

BLOCKSIZE = 15

SCREENWIDTH = BLOCKSIZE * WIDTH
SCREENHEIGHT = BLOCKSIZE * HEIGHT

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (200, 200, 200)
black = (0, 0, 0)

def find_path(maze, start, end, visited):
    if start == end:
        return True
    row, col = start
    if visited[row][col] or maze[row][col] == '#':
        return False
    visited[row][col] = True
    if maze[row - 1][col] != '#':
        if find_path(maze, (row - 1, col), end, visited):
            maze[row - 1][col] = '*'
            return True
    if maze[row + 1][col] != '#':
        if find_path(maze, (row + 1, col), end, visited):
            maze[row + 1][col] = '*'
            return True
    if maze[row][col - 1] != '#':
        if find_path(maze, (row, col - 1), end, visited):
            maze[row][col - 1] = '*'
            return True
    if maze[row][col + 1] != '#':
        if find_path(maze, (row, col + 1), end, visited):
            maze[row][col + 1] = '*'
            return True
    return False

def draw_maze(maze):
    top = 0
    left = 0
    for line in maze:
        for square in line:
            if square == '#':
                pygame.draw.rect(screen, blue, (left, top, BLOCKSIZE, BLOCKSIZE))
            elif square == '*':
                pygame.draw.rect(screen, red, (left, top, BLOCKSIZE, BLOCKSIZE))
            left += BLOCKSIZE
        left = 0
        top += BLOCKSIZE

pygame.init()
clock = pygame.time.Clock()

def get_coords():
    pixelx, pixely = pygame.mouse.get_pos()
    x, y = pixelx / BLOCKSIZE, pixely / BLOCKSIZE
    return x, y

current_end = get_coords()
previous_end = current_end

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_end = get_coords() 
    end_x, end_y = current_end
    if current_end != previous_end and maze[end_y][end_x] != '#':
        # reset maze
        maze = maze_copy[:]
        print '\n'.join([''.join(row) for row in maze])
        # set the previous end to 0
        maze[previous_end[1]][previous_end[0]] = ' '

        # fill the path with *
        visited = [[False] * WIDTH for i in range(HEIGHT)]
        find_path(maze, start, (current_end[1], current_end[0]), visited)

        # set current end to E
        maze[end_y][end_x] = 'E'

        previous_end = current_end

        #print '\n'.join([''.join(row) for row in maze])


    screen.fill(black)
    draw_maze(maze)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
