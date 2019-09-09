# coding=utf-8
# 笑脸弹跳游戏

import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
# step1. 载入图像
smilePic = pygame.image.load("smile.gif")

# colorkey = smilePic.get_at((0,0))
# smilePic.set_colorkey(colorkey)

# step2. 设置XY坐标移动起来
picX = 0
picY = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()
# speed = 5
speedX = 5
speedY = 5

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    picX += speedX
    picY += speedY

    # step3. 模拟碰到墙壁弹回
    if picX <= 0 or smilePic.get_width() + picX >= 800 :
        # 通过修改speed为负值，从而修改移动的方向
        # speed = -speed
        speedX = -speedX
    if picY <= 0 or smilePic.get_height() + picY >= 600 :
        speedY = -speedY

    # 解决用黑色像素填充屏幕，消除像素轨迹
    screen.fill(BLACK)
    # blit()方法把图像从硬盘加载绘制到显示界面上。当我们想要将像素从一个界面（如硬盘）复制到另一个界面（如绘制窗口）之上的时候就使用blit()
    screen.blit(smilePic,(picX,picY))
    pygame.display.update()
    timer.tick(60)

pygame.quit()

