import pygame
pygame.init()
import pygame
col = 50
line = 25
player_size_x = 2
player_size_y = 4
player = 1
bomb = 2
playerboard = []

for i in range(line):
    playerboard.append([])
    for j in range(col):
        playerboard[i].append(0)

pygame.init()
for i in playerboard:
    print(i)
screen = pygame.display.set_mode((col * 20 ,line * 20))
pygame.display.set_caption("ben and sked")
imp = pygame.image.load("pixil-frame-0.png")
imp = pygame.transform.scale(imp, ((player_size_x * 20,player_size_y * 20)))
running = True
while running:
    for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

    screen.fill("dark green")
    screen.blit(imp,(0,0))
    pygame.display.update()
