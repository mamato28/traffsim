import pygame
import random
import time

# Initialize Pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cars with Threads")

GREY = (196, 196, 196)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (114, 160, 91)
ORANGE = (255, 165, 0)

car_image_RL = pygame.image.load('pictures/car_left.png')
car_image_RL = pygame.transform.scale(car_image_RL, (90, 36))

car_image_LR = pygame.image.load('pictures/car_right.png')
car_image_LR = pygame.transform.scale(car_image_LR, (90, 36))

# car_image_UD1 = pygame.image.load('pictures/car_down.png')
# car_image_UD1 = pygame.transform.scale(car_image_UD1, (36, 90))

# car_image_UD2 = pygame.image.load('pictures/car_down.png')
# car_image_UD2 = pygame.transform.scale(car_image_UD2, (36, 90))



font_speed = pygame.font.Font(None, 24)

road_image = pygame.image.load('pictures/road.png')
road_image = pygame.transform.scale(road_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

class SmallCar():
    last_add_time = time.time()  # Class variable to track last add time
    next_add_time = last_add_time + random.randint(1, 2)  # Initialize the next add time

    def __init__(self, x, y, direction):
        self.width = 90
        self.height = 36
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = random.randint(1, 10)
        randomcolorR = random.randint(0, 255)
        randomcolorG = random.randint(0, 255)
        randomcolorB = random.randint(0, 255)
        self.color = (randomcolorR, randomcolorG, randomcolorB)

        self.original_y = y
        self.y_direction = 1  # Start by moving downwards or set to -1 to start upwards
        self.last_y_update_time = time.time()  # Track last time y-axis was updated
        

    def move(self):
        if self.direction == 'left':
            self.x -= self.speed  # Move left
        else:       # self.direction ==  'right'
            self.x += self.speed  # Move right

        
        if self.speed > 0:
            current_time = time.time()
            if current_time - self.last_y_update_time >= 2:  # Check if 2 seconds have passed
                # Move vertically within the range of original y ± 5 pixels
                if self.y <= self.original_y - 5:
                    self.y_direction = 1  # Move down
                elif self.y >= self.original_y + 5:
                    self.y_direction = -1  # Move up

                self.y += self.y_direction
                self.last_y_update_time = current_time  # Reset the timer


    def detectrange(self, other_cars):
        for car in other_cars:
            if car != self:
                if self.direction == 'left' and self.x > car.x and self.x - car.x <= 110:
                    self.speed = max(0, self.speed - 5)
                    return
                elif self.direction == 'right' and self.x < car.x and car.x - self.x <= 110:
                    self.speed = max(0, self.speed - 5)
                    return
        self.speed = random.randint(1, 10)
    
    @staticmethod
    def randomappear():
        appearpossibility = random.randint(1, 5)
        return appearpossibility > 1  # if > 3 return True, else return False
        
    @staticmethod
    def calculatelastadd():
        current_time = time.time()
        if current_time >= SmallCar.next_add_time:
            SmallCar.next_add_time = current_time + random.randint(1, 2)
            return True
        return False

            
    def stopatred(self, current_light):
        if self.direction == 'left':
            stop_line_x_min = SCREEN_WIDTH * 0.585
            stop_line_x_max = SCREEN_WIDTH * 0.600
            if current_light == 'red' and stop_line_x_min < self.x < stop_line_x_max:
                self.speed = 0
        else:
            stop_line_x_min = SCREEN_WIDTH * 0.350  # Adjusted for left-to-right traffic
            stop_line_x_max = SCREEN_WIDTH * 0.365
            if current_light == 'red' and stop_line_x_min < self.x < stop_line_x_max:
                self.speed = 0

    def draw(self, surface):
        # pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        if self.direction == 'left':
            surface.blit(car_image_RL, (self.x, self.y))
        elif self.direction == 'right':
            surface.blit(car_image_LR, (self.x, self.y))
        
        
        speed_text = font_speed.render(f'Speed: {self.speed}', True, BLACK)
        surface.blit(speed_text, (self.x + self.width // 2 - speed_text.get_width() // 2, self.y - 20))
        

# Initialize lists for cars
small_cars_right_to_left = []
small_cars_left_to_right = []


#==============================================================================



class SmallCar_UD():
    last_add_time = time.time()  # Class variable to track last add time
    next_add_time = last_add_time + random.randint(1, 2)  # Initialize the next add time

    def __init__(self, x, y, direction):
        self.car_image = pygame.image.load('pictures/car_down.png')
        self.car_width, self.car_height = self.car_image.get_size()
        self.width = 38
        self.height = 90
        self.x = SCREEN_WIDTH*0.5
        self.y = y
        self.direction = direction
        self.y_speed = random.randint(1, 10)
        self.x_speed = 5
        self.rotation_angle = 0
        self.rotation_speed = 5
        self.moving_down = True
        self.turning_direction = None
        self.timer_turn = 60    # for 60 seconds it wont change the turning direction, but it should vanish before 60 seconds
        # self.turn_decider = True
        
    def move_UD(self):
        if self.direction == 'down' :
            if self.moving_down :
                self.y += self.y_speed
                # 分left or right
                if self.y > SCREEN_HEIGHT*0.385:
                    self.moving_down = False
        
        # print(self.x)
    
    def choose_turning_direction_UD(self):
        if self.turning_direction is None:
            self.turn_direction = random.choice(['right', 'left'])

    def turn_after_choose_UD(self):
        if self.turn_direction == 'right' :
            self.turn_right_UD()
            self.timer_turn -= 1
            if self.timer_turn > 1:
                self.turning_direction = 'right'
        else:
            self.turn_left_UD()
            self.timer_turn -= 1
            if self.timer_turn > 1:
                self.turning_direction = 'left'
    

    def turn_left_UD(self):
        # print("Turning left")
        if self.rotation_angle < 90:
            self.rotation_angle += self.rotation_speed
        self.x += self.x_speed
        # print(self.x_speed)
        if self.y < SCREEN_HEIGHT*0.73:
            self.y += self.y_speed



    def turn_right_UD(self):
        # print(self.x)
        # print("Turning right")
        
        if self.y > SCREEN_HEIGHT*0.575:
            if self.rotation_angle > -90:
                self.rotation_angle -= self.rotation_speed

            if self.x > SCREEN_WIDTH*0.4 :
                self.x -= self.x_speed
            else :
                self.x_speed += random.uniform(-1, 1)
                self.x_speed = max(1, min(10, self.x_speed))
                self.x -= self.x_speed
        
        if self.y < SCREEN_HEIGHT * 0.62:
            self.y += self.y_speed


    def detectrange_UD(self, other_cars):
        if self.y <= SCREEN_HEIGHT*0.5:
            for car in other_cars:
                if car != self:
                    if self.direction == 'down' and self.y < car.y and car.y - self.y <= 110:  
                        self.y_speed = max(0, self.y_speed - 5)  # Stop the car to prevent overlap
                        return
            
            self.y_speed = random.randint(1, 10)

    
    def randomappear_UD():
        appearpossibility = random.randint(1, 5)
        return appearpossibility > 1  # if > 3 return True, else return False
        
    
    def calculatelastadd_UD():
        current_time = time.time()
        if current_time >= SmallCar_UD.next_add_time:
            SmallCar_UD.next_add_time = current_time + random.randint(1, 2)
            return True
        return False

            
    def stopatred_UD(self, current_light):
        if self.direction == 'down':
            stop_line_y_min = SCREEN_HEIGHT * 0.370
            stop_line_y_max = SCREEN_HEIGHT * 0.385
            if current_light == 'green' and stop_line_y_min < self.y < stop_line_y_max:
                self.y_speed = 0
    
    
    def draw_UD(self, screen):
        
        if self.direction == 'down':
            rotated_car = pygame.transform.rotate(self.car_image, self.rotation_angle)
                
                # Get the new rect for the rotated car image
            rotated_rect = rotated_car.get_rect(center=(self.x+15, self.y+50))
            
            # Draw the rotated car image
            screen.blit(rotated_car, rotated_rect.topleft)
            # if self.turn_decider:
            #     screen.blit(self.car_image, (self.x, self.y))
            #     if self.y > SCREEN_HEIGHT * 0.377 :
            #         self.turn_decider = False
            
            # if self.y > SCREEN_HEIGHT * 0.377 :
            #     rotated_car = pygame.transform.rotate(self.car_image, self.rotation_angle)
                
            #     # Get the new rect for the rotated car image
            #     rotated_rect = rotated_car.get_rect(center=(self.x, self.y))
                
            #     # Draw the rotated car image
            #     screen.blit(rotated_car, rotated_rect.topleft)
            
            # else:
            #     surface.blit(car_image_UD1, (self.x, self.y))
            speed_text = font_speed.render(f'Speed: {self.y_speed}', True, BLACK)
            screen.blit(speed_text, (self.x + self.width // 2 - speed_text.get_width() // 2, self.y))    


small_cars_up_to_down = []


#==============================================================================

start_time = time.time()

# Define the traffic light cycle times
green_time = 10  # seconds
orange_time = 1  # seconds
red_time = 10  # seconds

current_light = 'green'
font_light = pygame.font.Font(None, 36)

class TrafficLight:
    def __init__(self, screen, position, times, font_light):
        self.screen = screen
        self.position = position
        self.green_time, self.orange_time, self.red_time = times
        self.font_light = font_light
        self.current_light = 'green'
        self.start_time = time.time()
        self.remaining_time = self.green_time

    def draw_traffic_light(self):
        x, y = self.position
        pygame.draw.rect(self.screen, BLACK, (x+5, y+275, 50, 50)) # upper
        pygame.draw.rect(self.screen, BLACK, (x-300, y+625, 50, 50)) # lower


        # Determine the color of the traffic light
        light_color = GREEN if self.current_light == 'green' else ORANGE if self.current_light == 'orange' else RED

        # Draw the single traffic light circle
        pygame.draw.circle(self.screen, light_color, (x+30, y+300), 20)  # upper
        pygame.draw.circle(self.screen, light_color, (x-275, y+650), 20)  # lower

        # Draw the countdown timer
        text = self.font_light.render(str(self.remaining_time), True, BLACK)
        self.screen.blit(text, (x+30 - text.get_width() // 2, y+300 - text.get_height() // 2))
        self.screen.blit(text, (x-275 - text.get_width() // 2, y+650 - text.get_height() // 2))


    def update_light(self):
        elapsed_time = time.time() - self.start_time
        if self.current_light == 'green':
            self.remaining_time = max(0, self.green_time - int(elapsed_time))
        elif self.current_light == 'orange':
            self.remaining_time = max(0, self.orange_time - int(elapsed_time))
        elif self.current_light == 'red':
            self.remaining_time = max(0, self.red_time - int(elapsed_time))

        if self.current_light == 'green' and elapsed_time >= self.green_time:
            self.current_light = 'orange'
            self.start_time = time.time()
        elif self.current_light == 'orange' and elapsed_time >= self.orange_time:
            self.current_light = 'red'
            self.start_time = time.time()
        elif self.current_light == 'red' and elapsed_time >= self.red_time:
            self.current_light = 'green'
            self.start_time = time.time()

    def run(self):
        self.update_light()
        self.draw_traffic_light()

traffic_light = TrafficLight(screen, (830, 120), (green_time, orange_time, red_time), font_light)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(road_image, (0, 0))
    
    traffic_light.run()

    # Handle right-to-left cars
    if len(small_cars_right_to_left) > 20:
        small_cars_right_to_left.pop(0)  # Remove the first element if list size exceeds 20
    
    if len(small_cars_left_to_right) > 20:
        small_cars_left_to_right.pop(0)

    if len(small_cars_up_to_down) > 20:
        small_cars_up_to_down.pop(0)

    if SmallCar.calculatelastadd():
        if random.choice([True, False]):  # Randomly choose direction
            if len(small_cars_right_to_left) == 0 or small_cars_right_to_left[-1].x < SCREEN_WIDTH - 100:
                if SmallCar.randomappear():
                    small_cars_right_to_left.append(SmallCar(SCREEN_WIDTH, SCREEN_HEIGHT * 0.66875, direction='left'))
        else:
            if len(small_cars_left_to_right) == 0 or small_cars_left_to_right[-1].x > 100:
                if SmallCar.randomappear():
                    small_cars_left_to_right.append(SmallCar(0, SCREEN_HEIGHT * 0.785, direction='right'))

    if SmallCar_UD.calculatelastadd_UD():
        if len(small_cars_up_to_down) == 0 or small_cars_up_to_down[-1].y > 100 :
            if SmallCar_UD.randomappear_UD():
                small_cars_up_to_down.append(SmallCar_UD(SCREEN_WIDTH * 0.5, 0, direction='down'))
    
    
    for small_car in small_cars_right_to_left:
        small_car.draw(screen)
        small_car.detectrange(small_cars_right_to_left)
        small_car.stopatred(traffic_light.current_light)
        small_car.move()

    
    for small_car in small_cars_left_to_right:
        small_car.draw(screen)
        small_car.detectrange(small_cars_left_to_right)
        small_car.stopatred(traffic_light.current_light)
        small_car.move()

    for small_car in small_cars_up_to_down:
        small_car.move_UD()
        if not small_car.moving_down:
            small_car.choose_turning_direction_UD()
            small_car.turn_after_choose_UD()

            # small_car.turn_right_UD()

        
        small_car.detectrange_UD(small_cars_up_to_down)
        small_car.stopatred_UD(traffic_light.current_light)
        small_car.draw_UD(screen)
        

    pygame.display.flip()  # Update screen
    pygame.time.delay(1000 // 20)  # 20 FPS

# Quit Pygame
pygame.quit()
