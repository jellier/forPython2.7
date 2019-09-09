# coding=utf-8
# 生成100随机颜色、位置、大小的点
import random
import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
keep_going = True

color = [0]*100
pos = [0]*100
radius = [0]*100

for n in range(100):
    color[n] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pos[n] = (random.randint(0, 800), random.randint(0, 600))
    radius[n] = random.randint(10, 80)
    pygame.draw.circle(screen, color[n], pos[n], radius[n])

# 事件处理
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.display.update()

pygame.quit()