import pygame
col = 50
line = 25

player = 1
bomb = 2

playerboard = []

for i in range(line):
    playerboard.append([])
    for j in range(col):
        playerboard[i].append(0)


for i in playerboard:
    print(i)

pygame.init()
X = 600
Y = 600


scrn = pygame.display.set_mode((X, Y))


pygame.display.set_caption('image')


imp = pygame.image.load("pixil-frame-0.png.png").convert()


scrn.blit(imp, (0, 0))

# paint screen one time
pygame.display.flip()
status = True
while (status):


    for i in pygame.event.get():


        if i.type == pygame.QUIT:
            status = False

# deactivates the pygame library
pygame.quit()
