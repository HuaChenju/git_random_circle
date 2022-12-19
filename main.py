import pygame
import sys
import random
from color_funk import rand_color

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    clock = pygame.time.Clock()
    v, fps, r = 10, 10, 0
    size = width, height = 400, 400
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Крест')
    # формирование кадра:
    # draw(screen)
    #color = pygame.Color('yellow')
    running, drawing = True, False
    center = (0, 0)
    screen.fill((255, 255, 255))
    while running:
     #   screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(screen, rand_color(), event.pos, random.randint(3, 100))
               # drawing, r, center = True, 0, event.pos
       # if drawing:
        #    pygame.draw.circle(screen, (color), center, r)
         #    r += v
        pygame.display.flip()
        clock.tick(fps)
