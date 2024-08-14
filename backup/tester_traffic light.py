import pygame
import sys
import threading
import random
import time

pygame.init()

canvas_width = 1400
canvas_height = 800
screen = pygame.display.set_mode((canvas_width, canvas_height))

pygame.display.set_caption("Cars with Threads")

GREY = (196, 196, 196)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (114, 160, 91)
ORANGE = (255, 165, 0)

rect101 = pygame.Rect(100, 535, 90, 36)
rect102 = pygame.Rect(300, 535, 90, 36)
rect103 = pygame.Rect(500, 535, 90, 36)

green_time = 5
orange_time = 1
red_time = 7

speed101 = random.randint(10, 50)
speed102 = random.randint(10, 50)
speed103 = random.randint(10, 50)

car_image = pygame.image.load('small_car.png')
car_image = pygame.transform.scale(car_image, (90, 36))

road_image = pygame.image.load('road.png')
road_image = pygame.transform.scale(road_image, (canvas_width, canvas_height))

randomspeedlow101 = 5
randomspeedhigh101 = 10

current_light = 'green'

font = pygame.font.Font(None, 24)
font_light = pygame.font.Font(None, 36)

exit_threads = False

def move_rect101():
    global rect101, speed101, rect102, exit_threads, randomspeedlow101, randomspeedhigh101
    while not exit_threads:
        if current_light != 'red' or rect101.x < canvas_width * 0.585 or rect101.x > canvas_width * 0.6:
            rect101.x -= speed101
            if rect101.x < 0:
                rect101.x = canvas_width
            distance = abs(rect101.x - rect103.x)
            if distance <= 95:
                speed101 = 0
            elif distance > 100:
                speed101 = random.randint(randomspeedlow101, randomspeedhigh101)
        else:
            speed101 = 0
        pygame.time.delay(1000 // 10)

def move_rect102():
    global rect102, speed102, rect101, exit_threads
    while not exit_threads:
        if current_light != 'red' or rect102.x < canvas_width * 0.585 or rect102.x > canvas_width * 0.6:
            rect102.x -= speed102
            if rect102.x < 0:
                rect102.x = canvas_width
            distance = abs(rect102.x - rect101.x)
            if distance <= 95:
                speed102 = 0
            elif distance > 100:
                speed102 = random.randint(5, 10)
        else:
            speed102 = 0
        pygame.time.delay(1000 // 10)

def move_rect103():
    global rect103, speed103, rect102, exit_threads
    while not exit_threads:
        if current_light != 'red' or rect103.x < canvas_width * 0.585 or rect103.x > canvas_width * 0.6:
            rect103.x -= speed103
            if rect103.x < 0:
                rect103.x = canvas_width
            distance = abs(rect103.x - rect102.x)
            if distance <= 95:
                speed103 = 0
            elif distance > 100:
                speed103 = random.randint(5, 10)
        else:
            speed103 = 0
        pygame.time.delay(1000 // 10)

thread101 = threading.Thread(target=move_rect101)
thread102 = threading.Thread(target=move_rect102)
thread103 = threading.Thread(target=move_rect103)

thread101.start()
thread102.start()
thread103.start()

def draw_traffic_light(color, remaining_time):
    pygame.draw.rect(screen, GREY, (830, 120, 100, 300))
    pygame.draw.circle(screen, GREEN if color == 'green' else BLACK, (880, 170), 40)
    pygame.draw.circle(screen, ORANGE if color == 'orange' else BLACK, (880, 270), 40)
    pygame.draw.circle(screen, RED if color == 'red' else BLACK, (880, 370), 40)

    text = font_light.render(str(remaining_time), True, BLACK)
    if color == 'green':
        screen.blit(text, (880 - text.get_width() // 2, 170 - text.get_height() // 2))
    elif color == 'orange':
        screen.blit(text, (880 - text.get_width() // 2, 270 - text.get_height() // 2))
    elif color == 'red':
        screen.blit(text, (880 - text.get_width() // 2, 370 - text.get_height() // 2))
    
    pygame.display.flip()

def draw_slider(slider_rect, value, min_val, max_val):
    pygame.draw.rect(screen, GREY, slider_rect)
    handle_pos = (slider_rect.x + (value - min_val) / (max_val - min_val) * slider_rect.width, slider_rect.y + slider_rect.height // 2)
    pygame.draw.circle(screen, WHITE, handle_pos, 10)
    text = font.render(str(value), True, WHITE)
    screen.blit(text, (slider_rect.x, slider_rect.y - 30))

slider1_rect = pygame.Rect(50, 700, 200, 20)
slider2_rect = pygame.Rect(300, 700, 200, 20)

start_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_threads = True
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:
                if slider1_rect.collidepoint(event.pos):
                    randomspeedlow101 = int((event.pos[0] - slider1_rect.x) / slider1_rect.width * 50)
                elif slider2_rect.collidepoint(event.pos):
                    randomspeedhigh101 = int((event.pos[0] - slider2_rect.x) / slider2_rect.width * 50)

    screen.blit(road_image, (0, 0))

    screen.blit(car_image, (rect101.x, rect101.y))
    screen.blit(car_image, (rect102.x, rect102.y))
    screen.blit(car_image, (rect103.x, rect103.y))

    speed_text101 = font.render(f"{speed101}", True, WHITE)
    speed_text102 = font.render(f"{speed102}", True, WHITE)
    speed_text103 = font.render(f"{speed103}", True, WHITE)
    
    screen.blit(speed_text101, (rect101.x + 5, rect101.y + 5))
    screen.blit(speed_text102, (rect102.x + 5, rect102.y + 5))
    screen.blit(speed_text103, (rect103.x + 5, rect103.y + 5))

    elapsed_time = time.time() - start_time
    if current_light == 'green':
        remaining_time = max(0, green_time - int(elapsed_time))
    elif current_light == 'orange':
        remaining_time = max(0, orange_time - int(elapsed_time))
    elif current_light == 'red':
        remaining_time = max(0, red_time - int(elapsed_time))

    if current_light == 'green' and elapsed_time >= green_time:
        current_light = 'orange'
        start_time = time.time()
    elif current_light == 'orange' and elapsed_time >= orange_time:
        current_light = 'red'
        start_time = time.time()
    elif current_light == 'red' and elapsed_time >= red_time:
        current_light = 'green'
        start_time = time.time()

    draw_traffic_light(current_light, remaining_time)

    draw_slider(slider1_rect, randomspeedlow101, 0, 50)
    draw_slider(slider2_rect, randomspeedhigh101, 0, 50)

    pygame.time.Clock().tick(30)

    pygame.display.flip()
