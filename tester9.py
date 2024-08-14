import pygame
import random
import time

# 初始化 Pygame
pygame.init()

# 設置屏幕大小
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("cars with threads")

class SmallCar:
    last_add_time = time.time()  # Class variable to track last add time
    next_add_time = last_add_time + random.randint(1, 3)  # Initialize the next add time

    def __init__(self, x, y):
        self.width = 90
        self.height = 36
        self.x = x
        self.y = y
        self.speed = random.randint(1, 2)
        randomcolorR = random.randint(0, 255)
        randomcolorG = random.randint(0, 255)
        randomcolorB = random.randint(0, 255)
        self.color = (randomcolorR, randomcolorG, randomcolorB)

    def move(self):
        self.x -= self.speed  # 向左移動
    
    def detectrange(self, other_cars):
        for car in other_cars:
            if car != self and self.x > car.x and self.x - car.x <= 120:
                self.speed = 0
                return  # If this car needs to stop, no need to check further
        self.speed = random.randint(1, 2)  # Reset speed if no car in range

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    @staticmethod
    def randomappear():
        appearpossibility = random.randint(1, 5)
        return appearpossibility > 3

    @staticmethod
    def calculatelastadd():
        current_time = time.time()
        if current_time >= SmallCar.next_add_time:
            SmallCar.next_add_time = current_time + random.randint(1, 3)
            return True
        return False

# 創建一個物件實例
small_cars = []

# 主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 保持small_cars列表的大小不超過一定數量，例如10
    if len(small_cars) > 4:
        small_cars.pop(0)  # 刪除列表中的第一個元素
    
    # 添加新車
    if SmallCar.calculatelastadd():
        if len(small_cars) == 0 or small_cars[-1].x < SCREEN_WIDTH - 100:
            if SmallCar.randomappear():
                small_cars.append(SmallCar(SCREEN_WIDTH, SCREEN_HEIGHT * 0.66875))

    # 移動和檢測車輛
    for small_car in small_cars:
        small_car.detectrange(small_cars)
        small_car.move()
    
    # 渲染圖形
    screen.fill((0, 0, 0))  # 填充屏幕為黑色

    for small_car in small_cars:
        small_car.draw(screen)  # 繪製移動物件

    pygame.display.flip()  # 更新屏幕

    # 加入延遲，讓車子移動更平滑
    pygame.time.delay(50)

# 退出 Pygame
pygame.quit()
