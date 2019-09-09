# coding=utf-8
import pygame
# 每次调用pygame都要使用pygame.init()
pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True
radius = 50
while keep_going:
    # 此处for循环是处理用户能够在程序中出发的所有交互事件的地方
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.circle(screen,(0,255,0), (100,100),radius)
    pygame.display.update()
pygame.quit()





