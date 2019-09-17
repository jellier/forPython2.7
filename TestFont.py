# coding=utf-8
import pygame
import sys

pygame.init()

# print (pygame.font.get_default_font())
# 系统需要X11 支持
# my_font = pygame.font.SysFont("arial", 16)


# pygame对于字体的处理主要是pygame.font.Font()对象
# 绘制窗口
screen = pygame.display.set_mode((600, 400), 0, 32)
# 绘制背景
background = pygame.Surface(screen.get_size())
# 填充颜色
background.fill(color=(255, 255, 23))
# 创建字体对象
font = pygame.font.Font(None, 56)
# 文本与颜色
text = font.render("I love Python", 1, (255, 10, 10))
# 获取中心的坐标
center = (background.get_width() / 2, background.get_height() / 2)
# 获取设置后新的坐标区域
textpos = text.get_rect(center=center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 将字体填充到背景
    background.blit(text, textpos)
    # 将背景填充到窗口
    screen.blit(background, (0, 0))
    pygame.display.update()

# 要注意一下层级关系，先将文字填充到背景层上，然后再将背景填充到屏幕上

# 函数：
# pygame.font.init()  ——  初始化字体模块
# pygame.font.quit()  ——  还原字体模块
# pygame.font.get_init()  ——  检查字体模块是否被初始化
# pygame.font.get_default_font()  ——  获得默认字体的文件名
# pygame.font.get_fonts()  ——  获取所有可使用的字体
# pygame.font.match_font()  ——  在系统中搜索一种特殊的字体
# pygame.font.SysFont()  ——  从系统字体库创建一个 Font 对象
#
# 类：
# pygame.font.Font   ——  从一个字体文件创建一个 Font 对象

# 参考：
# https://www.pygame.org/docs/ref/font.html
# https://blog.csdn.net/qq_41556318/article/details/86303502
# https://blog.csdn.net/katyusha1/article/details/78357645
# https://eyehere.net/2011/python-pygame-novice-professional-4/

