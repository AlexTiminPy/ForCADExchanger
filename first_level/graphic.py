import time

import pygame
import sys

DX, DY = 350, 175

from Classes import *

ellipse1 = Ellipse(100, 50)

screen = pygame.display.set_mode((900, 450))
running = True

surface = pygame.Surface((200, 100))
red = (180, 50, 50)
size = (0, 0, 200, 100)

ellipse = pygame.draw.ellipse(surface, red, size)
angle = 0

while running:
    screen.fill((0, 0, 0))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(surface, (0 + DX, 0 + DY))
    coord = ellipse1.get_point_along_line(math.radians(angle))

    angle = math.degrees(math.atan2(mouse[1] - 225, mouse[0] - 450))

    pygame.draw.rect(screen, (0, 255, 255),
                     [coord.x + 100 + DX, coord.y + 50 + DY, 4, 4]
                     )

    pygame.draw.line(screen, (255, 255, 255),
                     [100 + DX, 50 + DY],
                     [200 * math.cos(math.radians(angle)) + 100 + DX,
                      200 * math.sin(math.radians(angle)) + 50 + DY], 3)

    coord_2 = ellipse1.get_derivative(math.radians(angle))

    pygame.draw.line(screen, (255, 255, 255),
                     [coord.x + 100 + DX, coord.y + 50 + DY],
                     [coord.x + 100 + DX + coord_2.x, coord.y + 50 + DY + coord_2.y],
                     3)

    pygame.draw.line(screen, (255, 255, 255),
                     [coord.x + 100 + DX, coord.y + 50 + DY],
                     [coord.x + 100 + DX - coord_2.x, coord.y + 50 + DY - coord_2.y],
                     3)

    pygame.display.update()
    time.sleep(0.015)
