####################
# 使用python进行下雪的演示
####################
from turtledemo import clock
# -*- coding: utf-8 -*-
import pygame
import random

# init
pygame.init()

# SIZE = (1920, 877)
# SIZE = (1280, 1024)
SIZE = (700, 500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Happy Valentine's Day!")


# load bitmap
backgroud = pygame.image.load("C:\\MySoftWare\\Pycharm\\PycharmTest\\snow\\snow_picture\\rose.jpg")
# 定义一个雪花列表
snow = []

# 初始化雪花
for i in range(500): # 此处的数字可以控制下雪的大小
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    speedx = random.randint(-1, 2)
    speedy = random.randint(1, 3)
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



