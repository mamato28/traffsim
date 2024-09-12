import pygame

# Initialize Pygame
pygame.init()

# Define constants for grid dimensions
GRID_WIDTH = 7
GRID_HEIGHT = 6
BLOCK_SIZE = 200
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (195, 195, 195)
FONT_COLOR = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid System")

# Load font
pygame.font.init()
font = pygame.font.SysFont(None, 40)

class World_Grid:
    def __init__(self, screen):
        self.screen = screen
        self.images = {}  # Dictionary to store images and their coordinates

    def add_image(self, image, coord):
        """Add an image to a specific grid block (1-indexed coordinates)."""
        self.images[coord] = image

    def draw_grid(self):
        """Draw a grid with blocks of 200x200 pixels, 7x6 blocks, label them with coordinates, and display images."""
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                # Draw a filled rectangle (no outline)
                rect = pygame.Rect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                # pygame.draw.rect(self.screen, WHITE, rect)  # Fill each block with white

                # Check if there is an image at this grid coordinate (1-indexed)
                if (col + 1, row + 1) in self.images:
                    image = self.images[(col + 1, row + 1)]
                    self.screen.blit(image, (col * BLOCK_SIZE, row * BLOCK_SIZE))

                # Draw grid lines (1px wide, on top of everything)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

                # Label the block with coordinates (1-indexed)
                coord_text = f"{col+1},{row+1}"
                text_surf = font.render(coord_text, True, FONT_COLOR)

                # Position the text at the center of each block
                text_rect = text_surf.get_rect(center=(col * BLOCK_SIZE + BLOCK_SIZE // 2,
                                                       row * BLOCK_SIZE + BLOCK_SIZE // 2))
                self.screen.blit(text_surf, text_rect)  # Draw the text

def load_and_add_images(world_grid):
    """Separate function to load and add multiple images to the grid."""
    # Load and resize images
    picA = pygame.image.load("v3/pictures_v3/road_stop_200.png")
    picA = pygame.transform.scale(picA, (BLOCK_SIZE, BLOCK_SIZE))
    
    picB = pygame.image.load("v3/pictures_v3/road_normal_200.png")
    picB = pygame.transform.scale(picB, (BLOCK_SIZE, BLOCK_SIZE))

    
    picA_rotated_90 = pygame.transform.rotate(picA, 90)
    picA_rotated_180 = pygame.transform.rotate(picA, 180)


    picC = pygame.image.load("v3/pictures_v3/grass_200.png")
    picC = pygame.transform.scale(picC, (BLOCK_SIZE, BLOCK_SIZE))

     
    # from right to left y=4
    world_grid.add_image(picA, (5, 4)) 

    world_grid.add_image(picB, (1, 4)) 
    world_grid.add_image(picB, (2, 4))  
    world_grid.add_image(picB, (3, 4)) 
    world_grid.add_image(picB, (6, 4)) 
    world_grid.add_image(picB, (7, 4)) 
    


    # from left to right y=5
    world_grid.add_image(picA_rotated_180, (3, 5))  

    world_grid.add_image(picB, (1, 5)) 
    world_grid.add_image(picB, (2, 5)) 
    world_grid.add_image(picB, (5, 5)) 
    world_grid.add_image(picB, (6, 5)) 
    world_grid.add_image(picB, (7, 5)) 
    


    # from up to down x=4
    world_grid.add_image(picA_rotated_90, (4, 3))  

    world_grid.add_image(picB, (4, 1)) 
    world_grid.add_image(picB, (4, 2)) 

    

    # middle cross
    world_grid.add_image(picB, (4, 4)) 
    world_grid.add_image(picB, (4, 5)) 
    

    # grass = picC
    world_grid.add_image(picC, (5, 1)) 
    world_grid.add_image(picC, (6, 1)) 
    world_grid.add_image(picC, (7, 1)) 




# Main loop
def main():
    clock = pygame.time.Clock()
    world_grid = World_Grid(screen)

    # Load and add images to the grid using the separate function
    load_and_add_images(world_grid)

    running = True

    while running:
        screen.fill(WHITE)
        world_grid.draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
