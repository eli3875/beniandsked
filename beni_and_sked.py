import pygame
from hey import *
pygame.init()
for i in playerboard:
    print(i)
screen = pygame.display.set_mode((col * 20 ,line * 20))
pygame.display.set_caption("ben and sked")
running = True
while running:
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False