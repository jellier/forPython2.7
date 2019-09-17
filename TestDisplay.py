# coding=utf-8
import pygame
from pygame.locals import *
from sys import exit


pygame.init()
# 可以用如下代码获得您的机器支持的显示模式：
print(pygame.display.list_modes())

background_img = 'data/sushiplate.jpg'

screen = pygame.display.set_mode([640, 480], RESIZABLE, 32)
background = pygame.image.load(background_img).convert()


Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # 全屏
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(
                        [640, 480], FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode([640, 480], 0, 32)

        # 窗口缩放
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)
            screen_width, screen_height = SCREEN_SIZE
            # 图片重新铺满窗口
            for y in range(0, screen_height, background.get_height()):
                for x in range(0, screen_width, background.get_width()):
                    screen.blit(background, (x, y))

        screen.blit(background, (0, 0))

    pygame.display.update()


# set_mode(size=(0, 0), flags=0, depth=0, display=0)
# The flags argument controls which type of display you want. There are several to choose from, and you can even combine multiple types using the bitwise or operator, (the pipe "|" character). If you pass 0 or no flags argument it will default to a software driven window. Here are the display flags you will want to choose from:
# pygame.FULLSCREEN    create a fullscreen display
# pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
# pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
# pygame.OPENGL        create an OpenGL-renderable display
# pygame.RESIZABLE     display window should be sizeable
# pygame.NOFRAME       display window will have no border or controls
# pygame.SCALED        resolution depends on desktop size and scale
# graphics--New in pygame 2.0.0

# 一般来说窗口就用0全屏就用FULLSCREEN，这两个总是OK的
# 如果你想创建一个硬件显示（surface会存放在显存里，从而有着更高的速度），你必须和全屏一起使用：
# screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | FULLSCREEN, 32)

# 当然你完全可以把双缓冲（更快）DOUBLEBUF也加上，这就是一个很棒的游戏显示了，
# 不过记得你要使用pygame.display.flip()来刷新显示。pygame.display.update()是将数据画到前面显示，而这个是交替显示的意思。
#
# 稍微说一下双缓冲的意思，可以做一个比喻：我的任务就是出黑板报，如果只有一块黑板，那我得不停的写，全部写完了稍微Show一下就要擦掉重写，这样一来别人看的基本都是我在写黑板报的过程，看到的都是不完整的黑板报；如果我有两块黑板，那么可以挂一块给别人看，我自己在底下写另一块，写好了把原来的换下来换上新的，这样一来别人基本总是看到完整的内容了。双缓冲就是这样维护两个显示区域，快速的往屏幕上换内容，而不是每次都慢慢地重画。
