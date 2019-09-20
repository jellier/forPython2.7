# coding=utf-8
# pygame.draw
# pygame.draw中函数的第一个参数总是一个surface，然后是颜色，再后会是一系列的坐标等。
# 稍有些计算机绘图经验的人就会知道，计算机里的坐标，(0，0)代表左上角。
# 而返回值是一个Rect对象，包含了绘制的领域，这样你就可以很方便的更新那个部分了。
import pygame
from sys import exit
from pygame.locals import *
import random
from math import pi

pygame.init()
screen = pygame.display.set_mode((640, 480),0,32)
point = []
BLACK = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # 按任意键清空屏幕
        if event.type ==KEYDOWN:
            point = []
            screen.fill(BLACK)
        # 按下鼠标开始画图
        if event.type == MOUSEBUTTONDOWN:
            screen.fill(BLACK)
            # 画随机矩形
            random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            random_pos = (random.randint(0,639), random.randint(0,479))
            random_wh = (639-random.randint(0,639), 479-random.randint(0,479))
            pygame.draw.rect(screen, random_color, Rect(random_pos,random_wh))
            # 画随机圆形
            random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            random_pos = (random.randint(0, 639), random.randint(0, 479))
            random_radius = random.randint(1, 200)
            pygame.draw.circle(screen, random_color, random_pos, random_radius)

            x, y = pygame.mouse.get_pos()
            point.append((x, y))
            # 根据点击位置画弧线
            # arc(surface, color, rect, start_angle, stop_angle, width=1)
            angle = (x / 639.) * pi * 2.
            pygame.draw.arc(screen, RED, (0, 0, 639, 479), 0, angle, 30)

            # 画椭圆
            pygame.draw.ellipse(screen,BLUE,(0, 0, x, y),10)

            # 从左上和右下画两根线连接到点击位置
            pygame.draw.line(screen, (0, 0, 255), (0, 0), (x, y))
            pygame.draw.line(screen, (255, 0, 0), (640, 480), (x, y))

            # lines(surface, color, closed, points, width=1)
            if len(point) > 1:
                pygame.draw.lines(screen,GREEN,False,point,3)

            # 把每个点画明显一点
            for p in point:
                pygame.draw.circle(screen, (155, 155, 155), p, 10)

    pygame.display.update()


# rect	绘制矩形
# polygon	绘制多边形（三个及三个以上的边）
# circle	绘制圆
# ellipse	绘制椭圆
# arc	绘制圆弧
# line	绘制线
# lines	绘制一系列的线
# aaline	绘制一根平滑的线
# aalines	绘制一系列平滑的线