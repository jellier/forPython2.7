# coding=utf-8

# pygame提供了字体处理，但是对中文的支持貌似不是很好！
import pygame
import sys

pygame.init()

# print (pygame.font.get_default_font())


# pygame.font.SysFont从系统字体库创建一个 Font 对象，系统需要X11 支持
# my_font = pygame.font.SysFont("arial", 16)


# pygame.font.Font()从一个字体文件创建一个 Font 对象，pygame对于字体的处理主要是使用Font对象
# 绘制窗口
screen = pygame.display.set_mode((600, 400), 0, 32)
# 绘制背景
background = pygame.Surface(screen.get_size())
# 填充颜色
background.fill(color=(255, 255, 23))
# 创建字体对象   pygame.font.Font("***.ttf", 字号)
font = pygame.font.Font(None, 56)
# 文本与颜色   pygame.font.Font.render(显示的内容，是否开启抗锯齿，字体颜色，字体背景颜色[可选])
text = font.render("I love Python", 1, (255, 10, 10))
# 获取中心的坐标
center = (background.get_width() / 2, background.get_height() / 2)
# 获取设置后新的坐标区域
# font也是一个surface对象！可以使用surface对象的方法,如get_rect()
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




# 使用自定义的字体：pygame.font.Font('data\\font\\TORK____.ttf', 20)
# 使用系统自带字体：pygame.font.SysFont("arial", 10)
# 相对而言自定义的字体要好一点，因为在pygame打包的过程中，可以把自定义的字体打包进去这样就可以进行很好的移植；
# 而系统自带的字体， 毕竟不是每个系统都有相应的字体，所以他的移植性不是很好，依赖性很大。


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
#
#方法：
# pygame.font.Font.render()  ——  在一个新 Surface 对象上绘制文本
# pygame.font.Font.size()  ——  确定多大的空间用于表示文本
# pygame.font.Font.set_underline()  ——  控制文本是否用下划线渲染
# pygame.font.Font.get_underline()  ——  检查文本是否绘制下划线
# pygame.font.Font.set_bold()  ——  启动粗体字渲染
# pygame.font.Font.get_bold()  ——  检查文本是否使用粗体渲染
# pygame.font.Font.set_italic()  ——  启动斜体字渲染
# pygame.font.Font.metrics()  ——  获取字符串参数每个字符的参数
# pygame.font.Font.get_italic()  ——  检查文本是否使用斜体渲染
# pygame.font.Font.get_linesize()  ——  获取字体文本的行高
# pygame.font.Font.get_height()  ——  获取字体的高度
# pygame.font.Font.get_ascent()  ——  获取字体顶端到基准线的距离
# pygame.font.Font.get_descent()  ——  获取字体底端到基准线的距离


# 参考：
# 官方：https://www.pygame.org/docs/ref/font.html
# font函数和方法详解：https://blog.csdn.net/qq_41556318/article/details/86303502
# 本示例来源：https://blog.csdn.net/katyusha1/article/details/78357645
# 另一个解释很清晰的示例：https://eyehere.net/2011/python-pygame-novice-professional-4/

