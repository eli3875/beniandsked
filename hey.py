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
