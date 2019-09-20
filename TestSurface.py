# coding=utf-8
# Surface是Pygame 中用于表示图像的对象
# 加载图片就是pygame.image.load，给它一个文件名然后就还给你一个surface对象。尽管读入的图像格式各不相同，surface对象隐藏了这些不同
# 屏幕也只是一个surface，pygame.display.set_mode就返回了一个屏幕surface对象。
# 指定尺寸创建一个空的surface，bland_surface = pygame.Surface((256, 256))
# Surface((width, height), flags=0, depth=0, masks=None)
# flag:
# ------HWSURFACE – 类似于前面讲的，更快！不过最好不设定，Pygmae可以自己优化。
# ------SRCALPHA – 有Alpha通道的surface，如果你需要透明，就要这个选项。这个选项的使用需要第二个参数为32

# 和pygame.draw一起使用时，作为draw.rect的第一参数，我理解是所有的图像都要先画在一个Surface对象上

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))

    screen.lock()    #很快你就会知道这两句lock和unlock的意思了
    for i in range(10):
        rand_pos = (randint(0, 639), randint(0, 479))
        screen.set_at(rand_pos, rand_col)
    screen.unlock()

    pygame.display.update()

# screen.lock()和screen.unlock()的作用
# 当Pygame往surface上画东西的时候，首先会把surface锁住，以保证不会有其它的进程来干扰，画完之后再解锁。锁和解锁时自动发生的，所以有时候可能不那么有效率，比如上面的例子，每次画100个点，那么就得锁解锁100次，现在我们把两句注释去掉，再执行看看是不是更快了（好吧，其实我没感觉出来，因为现在的机器性能都不错，这么点的差异还不太感觉的出来。不过请相信我~复杂的情况下会影响效率的）

# 参考：

# https://fishc.com.cn/forum.php?mod=viewthread&tid=62190
# 属性 & 方法
#
# pygame.Surface.blit()  —  将一个图像（Surface 对象）绘制到另一个图像上方
# pygame.Surface.convert()  —  修改图像（Surface 对象）的像素格式
# pygame.Surface.convert_alpha()  —  修改图像（Surface 对象）的像素格式，包含 alpha 通道
# pygame.Surface.copy()  —  创建一个 Surface 对象的拷贝
# pygame.Surface.fill()  —  使用纯色填充 Surface 对象
# pygame.Surface.scroll()  —  移动 Surface 对象
# pygame.Surface.set_colorkey()  —  设置 colorkeys
# pygame.Surface.get_colorkey()  —  获取 colorkeys
# pygame.Surface.set_alpha()  —  设置整个图像的透明度
# pygame.Surface.get_alpha()  —  获取整个图像的透明度
# pygame.Surface.lock()  —  锁定 Surface 对象的内存使其可以进行像素访问
# pygame.Surface.unlock()  —  解锁 Surface 对象的内存使其无法进行像素访问
# pygame.Surface.mustlock()  —   检测该 Surface 对象是否需要被锁定
# pygame.Surface.get_locked()  —  检测该 Surface 对象当前是否为锁定状态
# pygame.Surface.get_locks()  —  返回该 Surface 对象的锁定
# pygame.Surface.get_at()  —  获取一个像素的颜色值
# pygame.Surface.set_at()  —  设置一个像素的颜色值
# pygame.Surface.get_at_mapped()  —  获取一个像素映射的颜色索引号
# pygame.Surface.get_palette()  —   获取 Surface 对象 8 位索引的调色板
# pygame.Surface.get_palette_at()  —  返回给定索引号在调色板中的颜色值
# pygame.Surface.set_palette()  —  设置 Surface 对象 8 位索引的调色板
# pygame.Surface.set_palette_at()  —  设置给定索引号在调色板中的颜色值
# pygame.Surface.map_rgb()  —  将一个 RGBA 颜色转换为映射的颜色值
# pygame.Surface.unmap_rgb()  —  将一个映射的颜色值转换为 Color 对象
# pygame.Surface.set_clip()  —  设置该 Surface 对象的当前剪切区域
# pygame.Surface.get_clip()  —  获取该 Surface 对象的当前剪切区域
# pygame.Surface.subsurface()  —  根据父对象创建一个新的子 Surface 对象
# pygame.Surface.get_parent()  —  获取子 Surface 对象的父对象
# pygame.Surface.get_abs_parent()  —  获取子 Surface 对象的顶层父对象
# pygame.Surface.get_offset()  —  获取子 Surface 对象在父对象中的偏移位置
# pygame.Surface.get_abs_offset()  —  获取子 Surface 对象在顶层父对象中的偏移位置
# pygame.Surface.get_size()  —  获取 Surface 对象的尺寸
# pygame.Surface.get_width()  —  获取 Surface 对象的宽度
# pygame.Surface.get_height()  —  获取 Surface 对象的高度
# pygame.Surface.get_rect()  —  获取 Surface 对象的矩形区域
# pygame.Surface.get_bitsize()  —  获取 Surface 对象像素格式的位深度
# pygame.Surface.get_bytesize()  —  获取 Surface 对象每个像素使用的字节数
# pygame.Surface.get_flags()  —  获取 Surface 对象的附加标志
# pygame.Surface.get_pitch()  —  获取 Surface 对象每行占用的字节数
# pygame.Surface.get_masks()  —  获取用于颜色与映射索引号之间转换的掩码
# pygame.Surface.set_masks()  —  设置用于颜色与映射索引号之间转换的掩码
# pygame.Surface.get_shifts()  —  获取当位移动时在颜色与映射索引号之间转换的掩码
# pygame.Surface.set_shifts()  —  设置当位移动时在颜色与映射索引号之间转换的掩码
# pygame.Surface.get_losses()  —  获取最低有效位在颜色与映射索引号之间转换的掩码
# pygame.Surface.get_bounding_rect()  —  获取最小包含所有数据的 Rect 对象
# pygame.Surface.get_view()  —  获取 Surface 对象的像素缓冲区视图
# pygame.Surface.get_buffer()  —  获取 Surface 对象的像素缓冲区对象
# pygame.Surface._pixels_address  —  像素缓冲区地址