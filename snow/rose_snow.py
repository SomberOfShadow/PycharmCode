####################
# 使用python进行下雪的演示
####################
from turtledemo import clock
# -*- coding: utf-8 -*-
import pygame
import random
import base64
import os
from rose_png import *
from rose_png import img as rose

pic_name = "my_rose.png"
image = open(pic_name, 'wb')
image.write(base64.b64decode(rose))
image.close()

# init
pygame.init()

# SIZE = (1920, 877)
# SIZE = (1280, 1024)
SIZE = (700, 500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Happy Valentine's Day!")

# load bitmap
backgroud = pygame.image.load(pic_name)

# 用完（加载到程序里之后）删了就好
os.remove(pic_name)

# 定义一个雪花列表
snow = []

# 初始化雪花
for i in range(500): # 此处的数字可以控制下雪的大小
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    speedx = random.randint(0, 2)
    speedy = random.randint(2, 4)
    snow.append([x, y, speedx, speedy])
    # print("show[]:", snow)

done = False
while not done:
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 绘制位图
    screen.blit(backgroud, (0, 0))

    for i in range(len(snow)):
        # 绘制雪花， 颜色、位置、大小
        pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3])

        # 移动雪花位置，下一次循环起效
        snow[i][0] += snow[i][2]
        snow[i][1] += snow[i][3]

        # 如果雪花落出屏幕， 重设位置
        if snow[i][1] > SIZE[1]:
            snow[i][1] = random.randrange(-50, -10)
            snow[i][0] = random.randrange(0, SIZE[0])

    pygame.display.flip()
    # clock.tick(10)

pygame.quit()
