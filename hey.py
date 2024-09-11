import pygame
import random

col = 50
line = 25

player = 1
bomb = 2

player_board = []

for i in range(line):
    player_board.append([])
    for j in range(col):
        player_board[i].append(0)

for i in player_board:
    print(i)

pygame.init()
Y = col * 20
X = line * 20

index_benni_row = 0
index_benni_col = 0

screen = pygame.display.set_mode((Y, X))

#beniimg
player_size_x = 2
player_size_y = 4

pygame.display.set_caption('beni')
imp = pygame.image.load("pixil-frame-0.png").convert()
imp = pygame.transform.scale(imp, (player_size_x * 20, player_size_y * 20))

screen.blit(imp, (index_benni_row, index_benni_col))

#shaked
pygame.display.set_caption('shaked')
imp_sked = pygame.image.load("sked.png").convert()
imp_sked = pygame.transform.scale(imp_sked, (3 * 20, 4 * 20))


left_move = 0
right_move = 0
up_move = 0
down_move = 0
pygame.display.flip()

working = True
while working:

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            working = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and index_benni_row > 0:
        index_benni_row -= 1
        left_move+= 1




    if keys[pygame.K_RIGHT] and index_benni_row < Y - 40:
        index_benni_row += 1
        right_move+= 1



    if keys[pygame.K_UP] and index_benni_col > 0:
        index_benni_col -= 1
        up_move+= 1




    if keys[pygame.K_DOWN] and index_benni_col < X - 80:
        index_benni_col += 1
        down_move += 1






    screen.fill("dark green")
    screen.blit(imp, (index_benni_row, index_benni_col))
    screen.blit(imp_sked, (940, 420))
    pygame.display.update()

pygame.quit()
