# coding=utf-8
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480))

# ===========生成一个所有颜色组合的图片 start============
# # Surface 是Pygame 中用于表示图像的对象 Surface((width, height), flags=0, depth=0, masks=None)
# all_colors = pygame.Surface((4096, 4096), depth=24)
# # xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器
# for r in xrange(256):
#     print r + 1, "out of 256"
#     # & 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
#     x = (r & 15) * 256
#     # >> 左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
#     y = (r >> 4) * 256
#     for g in xrange(256):
#         for b in xrange(256):
#             # pygame.Surface.set_at()  —  设置一个像素的颜色值
#             all_colors.set_at((x + g, y + b), (r, g, b))
# pygame.image.save(all_colors, "allcolors.bmp")

# ===========生成一个所有颜色组合的图片 end=========

# =========三原色控制器 start=================


# step1.画红、绿、蓝三个色块
def creat_colorScale(height):
    screen_width = screen.get_size()[0]
    # ?
    red_scale_surface = pygame.surface.Surface((screen_width, height))
    green_scale_surface = pygame.surface.Surface((screen_width, height))
    blue_scale_surface = pygame.surface.Surface((screen_width, height))
    for x in range(screen_width):
        # x 的值是从0-639，screen_width=640,在正常的数学计算中 x/640=0.***
        # 但python中，两个整数相除会得到不带余数的整数，则0/640=0，所以要将其中一个数作为小数输入640.0
        c = int((x / float(screen_width)) * 255.0)
        # print ('x is %s, x/screen_width is %s'%(x, x/640.0))
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)

        # pygame.Rect(left, top, width, height)
        line_rect = Rect(x, 0, 1, height)

        # pygame.draw.rect(surface, color, rect, width=0)
        # ---- surface (Surface) -- surface to draw on
        # ---- rect (Rect) -- rectangle to draw, position and dimensions
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface


# step2. 初始化常量
red_scale, green_scale, blue_scale = creat_colorScale(80)
color = [127, 127, 127]


# step3. 画图
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # step3.1 将画好的矩形显示在屏幕上
    screen.fill((0, 0, 0))
    screen.blit(red_scale, (0, 0))
    screen.blit(green_scale, (0, 80))
    screen.blit(blue_scale, (0, 160))
    # 画下方色块，tuple() 函数将列表转换为元组
    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

    # step3.2 画颜色控制按钮
    for component in range(3):
        print((color[component] / 255.) * 639)
        pos = (int((color[component] / 255.) * 639), component * 80 + 40)
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    # step3.3 鼠标按下时，通过全局变量color更新下方色块颜色及标题
    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component * 80 and y < (component + 1) * 80:
                color[component] = int((x / 639.) * 255.)
        pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))

    pygame.display.update()

# =========三原色控制器 end=================
