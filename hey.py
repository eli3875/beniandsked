

import pygame
import random
import time
WON = False
BOMBA = False
col = 50
row = 25
Y = int(col * 20)
X = int(row * 20)
run = True

#
pygame.init()

screen = pygame.display.set_mode((Y, X))

rectungle = pygame.Rect(30, 30, 60, 60)

# #beniimg
player_size_x = 2
player_size_y = 4
#
pygame.display.set_caption('beni')
imp = pygame.image.load("pixil-frame-0.png")
imp = pygame.transform.scale(imp, (player_size_x * 20, player_size_y * 20))
index_benni_row = 0
index_benni_col = 0

#bomb
pygame.display.set_caption('Lin')
bomb_pic = pygame.image.load("IMG_3500.jpeg")
bomb_pic = pygame.transform.scale(bomb_pic, (1000,500))

#wiining
pygame.display.set_caption('Win')
WININGPIC = pygame.image.load("IMG_3506.png.jpeg")
WININGPIC = pygame.transform.scale(WININGPIC, (1000,500))



playerboard = []

for i in range(row):
    playerboard.append([])
    for j in range(col):
        playerboard[i].append(0)
        playerboard[index_benni_row][index_benni_col] = 1

bomb_list = []
for bomb_times in range(20):
    bomb_row = random.randint(0, 24)
    bomb_col = random.randint(0, 49)
    playerboard[bomb_row][bomb_col] = 2
    bomb_list.append((bomb_row, bomb_col))

imp_bomb = pygame.image.load("pixil-frame-0 (1).png")
imp_bomb = pygame.transform.scale(imp_bomb, (3 * 20, 1 * 20))

# shaked
pygame.display.set_caption('shaked')
shaked_size_width = 3
shaked_size_height = 4
imp_sked = pygame.image.load("sked.png")
imp_sked = pygame.transform.scale(imp_sked, (shaked_size_width * 20, shaked_size_height * 20))

for i in range(shaked_size_height):
    for j in range(shaked_size_width):
        playerboard[row - i - 1][col - j - 1] = 3

cotton_list = []
for cotton in range(20):
    cotton_row = random.randint(0, 24)
    cotton_col = random.randint(0, 49)
    playerboard[cotton_row][cotton_col] = 4
    cotton_list.append((cotton_row, cotton_col))
cotton_img = pygame.image.load("pixil-frame-0 (3).png")
cotton_img = pygame.transform.scale(cotton_img, (3 * 20, 3 * 20))
for w in playerboard:
    print(w)



for w in playerboard:
    print(w)
screen.blit(imp, (index_benni_row, index_benni_col))

working = True
while working:
    # screen.fill("dark green")
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            working = False

        if WON:
            print("won")
            working = False
            screen.blit(WININGPIC, (0, 0))
            pygame.display.update()
            time.sleep(4)

        if BOMBA:
            print("bomb!")
            screen.blit(bomb_pic, (0, 0))
            pygame.display.update()
            time.sleep(4)
            working = False




        keys = pygame.key.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            index_benni_col -= 1

            if index_benni_col < 0:
                index_benni_col = 0
            else:
                if playerboard[index_benni_row][index_benni_col] == 3:
                    WON = True
                if playerboard[index_benni_row][index_benni_col] == 2:
                    BOMBA = True

                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row][index_benni_col + 1] = 0


            for i in playerboard:
                print(i)
            print("----")
        if keys[pygame.K_RIGHT]:

            if index_benni_col < 48:
                index_benni_col += 1
                if playerboard[index_benni_row][index_benni_col] == 3:
                    WON = True
                if playerboard[index_benni_row][index_benni_col] == 2:
                    BOMBA = True

                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row][index_benni_col - 1] = 0



            else:
                index_benni_col = 48

            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_UP]:

            if index_benni_row == 0:
                index_benni_row = 0


            else:
                index_benni_row -= 1
                if playerboard[index_benni_row][index_benni_col] == 3:
                    WON = True
                if playerboard[index_benni_row][index_benni_col] == 2:
                    BOMBA = True
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row + 1][index_benni_col] = 0

                




            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_DOWN]:

            if index_benni_row == 24:
                index_benni_row = 24


            else:

                index_benni_row += 1
                if playerboard[index_benni_row][index_benni_col] == 3:
                    WON = True
                if playerboard[index_benni_row][index_benni_col] == 2:
                    BOMBA = True
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row - 1][index_benni_col] = 0

            for w in playerboard:
                print(w)
            print("----")

        if keys[pygame.K_END] :
            screen.fill("dark grey")

            for rows in range(0, 1010, int(1000 / 50)):
                for cols in range(0, 510, int(500 / 25)):
                    rect11 = pygame.Rect(0, 0, rows, cols)
                    for i in bomb_list:
                        screen.blit(imp_bomb, ((i[1] * 1000 / 50), i[0] * 500 / 25))

                    pygame.draw.rect(screen, "black", rect11, 1)
                    screen.blit(imp, (index_benni_col * 20, index_benni_row * 20))
                    screen.blit(imp_sked, (940, 420))

                    pygame.display.update()
            time.sleep(1)
        pygame.display.update()



        screen.fill("dark green")
        for i in cotton_list:
            screen.blit(cotton_img, ((i[1] * 1010 / 50), i[0] * 510 / 25))
        screen.blit(imp, (index_benni_col * 20, index_benni_row * 18))
        screen.blit(imp_sked, (940, 420))
        pygame.display.update()
        pygame.display.update()
pygame.quit()
