import pygame

# 初始化pygame
pygame.init()

# 設定視窗大小和矩形大小
window_size = (300, 300)  # 整個視窗大小
rect_width = 90
rect_height = 40
square_size = 100

# 設定顏色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 創建視窗
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("矩形移動")

# 初始化矩形的位置
rect_x = 100 + (square_size - rect_width) / 2  # 將矩形水平居中放置
rect_y = 100 + square_size - rect_height  # 矩形初始放在正方形的底部

# 定義移動速度
move_speed = 2
moving_up = True
moving_right = False

# 主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景
    screen.fill(WHITE)

    # 繪製100px的正方形框線
    pygame.draw.rect(screen, BLUE, (100, 100, square_size, square_size), 2)

    # 控制矩形的移動
    if moving_up:
        rect_y -= move_speed  # 向上移動
        if rect_y <= 100:  # 到達正方形頂端
            moving_up = False
            moving_right = True  # 開始水平移動
    elif moving_right:
        rect_x += move_speed  # 向右移動
        if rect_x + rect_width >= 100 + square_size:  # 到達右邊界
            moving_right = False

    # 繪製矩形
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # 更新顯示
    pygame.display.flip()

    # 控制幀率
    pygame.time.Clock().tick(60)

# 結束pygame
pygame.quit()