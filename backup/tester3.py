import pygame
import sys
import threading
import random
import time

pygame.init()

canvas_width = 1400
canvas_height = 800
screen = pygame.display.set_mode((canvas_width, canvas_height))

pygame.display.set_caption("cars with threads")

GREY = (196, 196, 196)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (114, 160, 91)
ORANGE = (255, 165, 0)

font = pygame.font.Font(None, 24)
font_light = pygame.font.Font(None, 36)

car_image = pygame.image.load('small_car.png')
car_image = pygame.transform.scale(car_image, (90, 36))

road_image = pygame.image.load('road.png')
road_image = pygame.transform.scale(road_image, (canvas_width, canvas_height))


################################################################################################

start_time = time.time()

# Define the traffic light cycle times
green_time = 5  # seconds
orange_time = 1  # seconds
red_time = 5  # seconds

current_light = 'green'

def draw_traffic_light(color, remaining_time):
    # Draw the traffic light frame traffic light left to right
    pygame.draw.rect(screen, GREY, (862, 335, 35, 100))

    # Draw the lights
    pygame.draw.circle(screen, GREEN if color == 'green' else BLACK, (880, 355), 11)
    pygame.draw.circle(screen, ORANGE if color == 'orange' else BLACK, (880, 385), 11)
    pygame.draw.circle(screen, RED if color == 'red' else BLACK, (880, 415), 11)

    # Draw traffic light right to left

    pygame.draw.rect(screen, GREY, (532, 680, 35, 100))

    pygame.draw.circle(screen, GREEN if color == 'green' else BLACK, (550, 700), 11)
    pygame.draw.circle(screen, ORANGE if color == 'orange' else BLACK, (550, 730), 11)
    pygame.draw.circle(screen, RED if color == 'red' else BLACK, (550, 760), 11)



    # Draw the countdown timer
    text = font_light.render(str(remaining_time), True, BLACK)
    if color == 'green':
        screen.blit(text, (880 - text.get_width() // 2, 355 - text.get_height() // 2))
        screen.blit(text, (550 - text.get_width() // 2, 700 - text.get_height() // 2))
    elif color == 'orange':
        screen.blit(text, (880 - text.get_width() // 2, 385 - text.get_height() // 2))
        screen.blit(text, (550 - text.get_width() // 2, 730 - text.get_height() // 2))
    elif color == 'red':
        screen.blit(text, (880 - text.get_width() // 2, 415 - text.get_height() // 2))
        screen.blit(text, (550 - text.get_width() // 2, 760 - text.get_height() // 2))
    
    # Update the display
    pygame.display.flip()




################################################################################################


rect101 = pygame.Rect(100, 535, 90, 36)  # x, y, width, height
rect102 = pygame.Rect(250, 535, 90, 36)
rect103 = pygame.Rect(400, 535, 90, 36)
rect104 = pygame.Rect(550, 535, 90, 36)
rect105 = pygame.Rect(700, 535, 90, 36)

speed101 = [random.randint(10, 50)]
speed102 = [random.randint(10, 50)]
speed103 = [random.randint(10, 50)]
speed104 = [random.randint(10, 50)]
speed105 = [random.randint(10, 50)]

rectangles = [
    (rect101, speed101, rect105, (5, 20)), 
    (rect102, speed102, rect101, (5, 20)),
    (rect103, speed103, rect102, (5, 20)),
    (rect104, speed104, rect103, (5, 20)),
    (rect105, speed105, rect104, (5, 20))
]

speed_texts = [
    font.render(f"{speed101[0]}", True, WHITE),
    font.render(f"{speed102[0]}", True, WHITE),
    font.render(f"{speed103[0]}", True, WHITE),
    font.render(f"{speed104[0]}", True, WHITE),
    font.render(f"{speed105[0]}", True, WHITE)
]
font = pygame.font.Font(None, 24)

# Create a shared variable to signal thread exit
exit_threads = False

# Store the new positions for rectangles that pass x <= 100


new_positions = [(100, 400), (100, 350), (100, 300), (100, 250), (100, 200), (100, 150)]
occupied_positions = []
# reset_value = 1
def move_rect(rect, speed, other_rect, canvas_width, speed_range, exit_threads, font, speed_texts, index, WHITE, rectangles):
    global occupied_positions, reset_value
    stop_moving = False
    while not exit_threads:
        if not stop_moving:
            if current_light != 'red' or rect.x < canvas_width * 0.585 or rect.x > canvas_width * 0.6:
                rect.x -= speed[0]
                if rect.x <= 50:
                    if len(occupied_positions) < len(new_positions):
                        rect.x, rect.y = new_positions[len(occupied_positions)]
                        occupied_positions.append((rect.x, rect.y))
                        speed[0] = 0  # Stop the rectangle at the new position
                        stop_moving = True  # Indicate that this rectangle should stop moving
                    else:
                        rect.x = canvas_width

                distance = abs(rect.x - other_rect.x)
                if rect.y == other_rect.y and distance <= 150:
                    speed[0] = max(0, speed[0] - 6)  # Gradually slow down
                elif rect.y == other_rect.y and distance > 150:
                    speed[0] = random.randint(*speed_range)
            else:
                speed[0] = max(0, speed[0] - 6)

        
            
            
            
            
            


        # Update speed text
        speed_texts[index] = font.render(f"{index}:{speed[0]}", True, WHITE)

        pygame.time.delay(1000 // 10)  # 10 FPS

# Create and start threads for each rectangle
threads = []
for index, (rect, speed, other_rect, speed_range) in enumerate(rectangles):
    thread = threading.Thread(target=move_rect, args=(rect, speed, other_rect, canvas_width, speed_range, exit_threads, font, speed_texts, index, WHITE, rectangles))
    threads.append(thread)
    thread.start()




################################################################################################
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_threads = True  # Signal threads to exit
            pygame.quit()
            sys.exit()
    
    screen.blit(road_image, (0, 0))

    screen.blit(car_image, (rect101.x, rect101.y)) 
    screen.blit(car_image, (rect102.x, rect102.y)) 
    screen.blit(car_image, (rect103.x, rect103.y))
    screen.blit(car_image, (rect104.x, rect104.y))
    screen.blit(car_image, (rect105.x, rect105.y))

    # Display speed inside each rectangle
    screen.blit(speed_texts[0], (rect101.x + 5, rect101.y + 5))
    screen.blit(speed_texts[1], (rect102.x + 5, rect102.y + 5))
    screen.blit(speed_texts[2], (rect103.x + 5, rect103.y + 5))
    screen.blit(speed_texts[3], (rect104.x + 5, rect104.y + 5))
    screen.blit(speed_texts[4], (rect105.x + 5, rect105.y + 5))

    # Calculate the time elapsed and remaining time
    elapsed_time = time.time() - start_time
    if current_light == 'green':
        remaining_time = max(0, green_time - int(elapsed_time))
    elif current_light == 'orange':
        remaining_time = max(0, orange_time - int(elapsed_time))
    elif current_light == 'red':
        remaining_time = max(0, red_time - int(elapsed_time))

    # Change the light based on the elapsed time
    if current_light == 'green' and elapsed_time >= green_time:
        current_light = 'orange'
        start_time = time.time()
    elif current_light == 'orange' and elapsed_time >= orange_time:
        current_light = 'red'
        start_time = time.time()
    elif current_light == 'red' and elapsed_time >= red_time:
        current_light = 'green'
        start_time = time.time()

    # Draw the current light with countdown timer
    draw_traffic_light(current_light, remaining_time)

    # Cap the frame rate
    pygame.time.Clock().tick(30)

    # Update the screen
    pygame.display.flip()
