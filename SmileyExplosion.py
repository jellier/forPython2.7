# coding=utf-8
# 笑脸爆炸
# 精灵图形的使用 pygame.sprite.Sprite类
import pygame
import random
pygame.init()
BLACK = (0, 0, 0)
# step1. 页面初始化：设置屏幕，设置标题，变量，初始化clock类，加载笑脸图片，初始化精灵类Group
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Smiley Explosion')
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load('smile.gif')
# colorkey = pic.get_at((0,0))
# pic.set_colorkey(colorkey)
spriteList = pygame.sprite.Group()


class Smiley(pygame.sprite.Sprite):
    # step2. 创建自己的精灵类，extend from pygame.sprite.Sprite
    # step2.1 初始化Smiley类的变量：位置、速率velocity（横向和纵向）、缩放比例
    pos = (0, 0)
    xVel = 1
    yVel = 1
    scale =100

    # step2.2 初始化函数
    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.rect = self.image.get_rect()
        self.pos = pos
        # 把精灵外边框中心和鼠标对齐，pos为对象实例传入的鼠标位置
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2
        self.xvel = self.xVel
        self.yvel = self.yVel

    # step2.3 根据每个精灵的速度来更改其位置并且检查是否与边缘碰撞
    def update(self):
        # self.rect.x/y 代表精灵的(x,y)位置
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel
        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.yvel = -self.yvel

# step3. 实例化
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

    screen.fill(BLACK)
    # update和draw两个方法是sprite.Group类自带的两个方法，更新、绘制group中的每一个对象
    spriteList.update()
    spriteList.draw(screen)

    clock.tick(60)
    pygame.display.update()

    if mousedown:
        speedX = random.randint(-5, 5)
        speedY = random.randint(-5, 5)
        newSmiley = Smiley(pygame.mouse.get_pos(),speedX, speedY)
        spriteList.add(newSmiley)

pygame.quit()





# pygame 几个常用的类：
# Clock类
# Sprite类
# Group类
