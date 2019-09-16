# coding=utf-8
import pygame
from pygame.locals import *
from sys import exit


pygame.init()
# 可以用如下代码获得您的机器支持的显示模式：
print (pygame.display.list_modes())

background_img = 'data/sushiplate.jpg'

screen = pygame.display.set_mode( [640,480],RESIZABLE, 32)
background = pygame.image.load(background_img).convert()

# ======全屏 start========
Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # 全屏
        if event.type == KEYDOWN:
            if event.key ==K_f :
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen =  pygame.display.set_mode( [640,480], FULLSCREEN, 32)
                else:
                    screen =  pygame.display.set_mode( [640,480],0, 32)

        # 窗口缩放
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)
            screen_width, screen_height = SCREEN_SIZE
            # 图片重新铺满窗口
            for y in range(0, screen_height,background.get_height()):
                for x in range(0, screen_width,background.get_width()):
                    screen.blit(background,(x,y))

        screen.blit(background, (0, 0))

    pygame.display.update()
# ======全屏 end========


# set_mode(size=(0, 0), flags=0, depth=0, display=0)
# The flags argument controls which type of display you want. There are several to choose from, and you can even combine multiple types using the bitwise or operator, (the pipe "|" character). If you pass 0 or no flags argument it will default to a software driven window. Here are the display flags you will want to choose from:
# pygame.FULLSCREEN    create a fullscreen display
# pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
# pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
# pygame.OPENGL        create an OpenGL-renderable display
# pygame.RESIZABLE     display window should be sizeable
# pygame.NOFRAME       display window will have no border or controls
# pygame.SCALED        resolution depends on desktop size and scale graphics--New in pygame 2.0.0