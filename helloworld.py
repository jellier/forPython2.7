# coding=utf-8
import pygame
# 导入一些常用的函数和常量
from pygame.locals import *
from sys import exit
#向sys模块借一个exit模块来控制退出
pygame.init()

background_img = 'data/sushiplate.jpg'
mouse_img = 'data/smile.gif'

screen = pygame.display.set_mode( [640,480],0, 32)

pygame.display.set_caption("Hello World!")

# convert函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件（事实上因为 它太常用了，如果你不写pygame也会帮你做）；
# convert_alpha相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。
background = pygame.image.load(background_img).convert()
mouse_cursor = pygame.image.load(mouse_img).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    # 画背景
    #blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用update更新一下，否则画面一片漆黑。
    screen.blit(background,(0, 0))

    # 画鼠标
    #获得鼠标位置
    x,y = pygame.mouse.get_pos()
    # 得到光标左上角坐标
    x = x - mouse_cursor.get_width()/2
    y = y - mouse_cursor.get_height()/2

    screen.blit(mouse_cursor,(x , y))


    pygame.display.update()