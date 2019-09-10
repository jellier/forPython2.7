# coding=utf-8
import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])

# 点击鼠标左键在屏幕上画图
# pygame.display.set_caption('Click to draw')
#
# keep_going = True
# RED = (255, 0, 0)
# radius = 20
#
# while keep_going:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             keep_going = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pos = event.pos
#             pygame.draw.circle( screen,RED, pos, radius)
#     pygame.display.update()
# pygame.quit()

#拖动鼠标画图
pygame.display.set_caption('Drag to draw')

keep_going = True
GREEN = (0, 255, 0)
radius = 15

mousedown = False

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

        if mousedown:
            pos = pygame.mouse.get_pos() # 此处与点击画图不同，get_pos()直接获取鼠标当前位置，而不是上一次点击位置
            pygame.draw.circle(screen,GREEN, pos, radius)
    pygame.display.update()
pygame.quit()