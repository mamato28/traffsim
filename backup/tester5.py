import pygame
import threading

# 初始化pygame
pygame.init()

# 設置屏幕大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 矩形的初始位置列表
rect_positions = [[600, 300], [700, 300], [800, 300]]
SPEED = 5
RECT_WIDTH, RECT_HEIGHT = 90, 50

# 主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # 清屏

    # 更新並繪製所有矩形
    for rect_pos in rect_positions:
        rect_pos[0] -= SPEED  # 更新位置
        if rect_pos[0] < -RECT_WIDTH:
            rect_pos[0] = SCREEN_WIDTH  # 矩形移動到屏幕左邊時重置位置
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(rect_pos[0], rect_pos[1], RECT_WIDTH, RECT_HEIGHT))

    pygame.display.flip()  # 更新屏幕顯示
    pygame.time.delay(16)  # 控制更新速度

pygame.quit()