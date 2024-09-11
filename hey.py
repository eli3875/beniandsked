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
X = col * 20
Y = line * 20

index_benni_row = 0
index_benni_col = 0

scrn = pygame.display.set_mode((X, Y))

#beni
pygame.display.set_caption('image')
imp = pygame.image.load("pixil-frame-0.png").convert()


scrn.blit(imp, (index_benni_row, index_benni_col))

# paint screen one time
pygame.display.flip()
status = True
while (status):


    for i in pygame.event.get():


        if i.type == pygame.QUIT:
            status = False

# deactivates the pygame library
pygame.quit()
