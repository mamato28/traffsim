import pygame
import random
import time

# 初始化 Pygame
pygame.init()

# 設置屏幕大小
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("cars with threads")

class SmallCar():
    def __init__(self, x, y):
        self.width = 90
        self.height = 36
        self.x = x
        self.y = y
        self.speed = 2
        randomcolorR = random.randint(0, 255)
        randomcolorG = random.randint(0, 255)
        randomcolorB = random.randint(0, 255)
        self.color = (randomcolorR, randomcolorG, randomcolorB)

    def move(self):
        self.x -= self.speed  # 向左移動
        if self.x < -self.width:  # 如果物件完全離開屏幕
            self.x = SCREEN_WIDTH  # 重置到右側
            self.speed = random.randint(1,3)  # 隨機新的速度
        

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

# 創建一個物件實例
small_cars = []
small_cars.append(SmallCar(SCREEN_WIDTH, SCREEN_HEIGHT * 0.66875))

# 控制添加車輛的計數器
car_spawn_counter = 0
car_spawn_interval = 60  # 每60幀添加一輛車

# 創建一個時鐘對象
clock = pygame.time.Clock()

# 主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 保持small_cars列表的大小不超過一定數量，例如10
    if len(small_cars) > 4:
        small_cars.pop(0)  # 刪除列表中的第一個元素

    # 更新遊戲邏輯
    if small_cars[-1].x <= 0:
        car_spawn_counter += 1
        if car_spawn_counter >= car_spawn_interval:
            if len(small_cars) == 0 or (SCREEN_WIDTH - small_cars[-1].x) > 120:
                small_cars.append(SmallCar(SCREEN_WIDTH, SCREEN_HEIGHT * 0.66875))
                car_spawn_counter = 0  # 重置計數器

    # for small_car in small_cars:
    #     small_car.move()
    
    for i in range(len(small_cars)):
        if i > 0:  # 從第二個車輛開始檢查
            distance = small_cars[i-1].x - small_cars[i].x
            if distance <= 150:
                small_cars[i].speed = 0
            elif distance > 150 and small_cars[i].speed == 0:
                small_cars[i].speed = random.randint(1, 3)  # 恢復原本的速度

        small_cars[i].move()


    # 渲染圖形
    screen.fill((0, 0, 0))  # 填充屏幕為黑色
    for small_car in small_cars:
        small_car.draw(screen)  # 繪製移動物件

    pygame.display.flip()  # 更新屏幕
    clock.tick(60)

# 退出 Pygame
pygame.quit()
