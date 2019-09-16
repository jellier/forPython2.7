# coding=utf-8

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode([640,480], 0, 32)

# font = pygame.font.SysFont("arial", 16);

while True:

    # pygame.event.get()来处理所有的事件，这好像打开大门让所有的人进入。
    # 如果我们使用pygame.event.wait()，Pygame就会等到发生一个事件才继续下去
    # pygame.event.poll()就好一些，一旦调用，它会根据现在的情形返回一个真实的事件，或者一个“什么都没有”
    event = pygame.event.wait()
    # 打印事件
    print(event)
    # 打印鼠标位置
    # print(event.pos)

    if event.type == QUIT:
        exit()
    screen.fill((0, 0, 0))

    pygame.display.update()






# 常用事件集：

# QUIT	用户按下关闭按钮	none
# ATIVEEVENT	Pygame被激活或者隐藏	gain, state
# KEYDOWN	键盘被按下	unicode, key, mod
# KEYUP	键盘被放开	key, mod
# MOUSEMOTION	鼠标移动	pos, rel, buttons
# MOUSEBUTTONDOWN	鼠标按下	pos, button
# MOUSEBUTTONUP	鼠标放开	pos, button
# JOYAXISMOTION	游戏手柄(Joystick or pad)移动	joy, axis, value
# JOYBALLMOTION	游戏球(Joy ball)?移动	joy, axis, value
# JOYHATMOTION	游戏手柄(Joystick)?移动	joy, axis, value
# JOYBUTTONDOWN	游戏手柄按下	joy, button
# JOYBUTTONUP	游戏手柄放开	joy, button
# VIDEORESIZE	Pygame窗口缩放	size, w, h
# VIDEOEXPOSE	Pygame窗口部分公开(expose)?	none
# USEREVENT	触发了一个用户事件	code