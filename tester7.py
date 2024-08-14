import pygame
import random


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
    
    def newcar(self):
        self.x = SCREEN_WIDTH
        self.speed = random.randint(1,3)

    def detectrange(self):
        if self.x - small_cars[-1].x <= 120 :
            self.speed = 0
        else:
            self.speed = random.randint(1,3)
    
    def waitforlight():
        pass
        # if self.x - small_cars[-1].x <= 120 :if current_light != 'red' or rect.x < canvas_width * 0.585 or rect.x > canvas_width * 0.6:

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

# 創建一個物件實例
small_cars = []
# small_cars.append(SmallCar(SCREEN_WIDTH, SCREEN_HEIGHT * 0.66875))




# 主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 保持small_cars列表的大小不超過一定數量，例如10
    if len(small_cars) > 4:
        small_cars.pop(0)  # 刪除列表中的第一個元素

    
    if len(small_cars) == 0 :
        small_cars.append(SmallCar(SCREEN_WIDTH, SCREEN_HEIGHT * 0.66875))
        SmallCar.move()
    
    
    


    # 渲染圖形
    screen.fill((0, 0, 0))  # 填充屏幕為黑色

    for small_car in small_cars:
        small_car.draw(screen)  # 繪製移動物件

    pygame.display.flip()  # 更新屏幕
    

# 退出 Pygame
pygame.quit()
