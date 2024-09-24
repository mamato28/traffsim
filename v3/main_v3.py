import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define constants for grid dimensions
GRID_WIDTH = 14
GRID_HEIGHT = 12
BLOCK_SIZE = 100
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (195, 195, 195)
BROWN = (155, 103, 60)
FONT_COLOR = (0, 0, 0)

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
        self.intersections = {}  # Dictionary to store intersection blocks and their movement options


    def add_image(self, image, coord):
        """Add an image to a specific grid block (1-indexed coordinates)."""
        self.images[coord] = image

    def add_intersection(self, coord, directions):
        """Define an intersection block and its possible movement directions."""
        self.intersections[coord] = directions

    def check_intersection(self, coord):
        """Check if the current block is an intersection and return possible directions."""
        if coord in self.intersections:
            return self.intersections[coord]
        return None


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

    picA_rotated_90 = pygame.transform.rotate(picA, 90)
    picA_rotated_180 = pygame.transform.rotate(picA, 180)
    
    # picB = normal road
    picB = pygame.image.load("v3/pictures_v3/road_normal_200.png")
    picB = pygame.transform.scale(picB, (BLOCK_SIZE, BLOCK_SIZE))

    # picC = grass
    picC = pygame.image.load("v3/pictures_v3/grass_200.png")
    picC = pygame.transform.scale(picC, (BLOCK_SIZE, BLOCK_SIZE))

     
    # from right to left y=4
    world_grid.add_image(picA, (5, 4)) 

    # from left to right y=5
    world_grid.add_image(picA_rotated_180, (3, 5))  

    # from up to down x=4
    world_grid.add_image(picA_rotated_90, (4, 3))  


    # middle cross
    world_grid.add_image(picB, (4, 4)) 
    world_grid.add_image(picB, (4, 5)) 
    

    
    # picB = normal road
    coords_normal_road = [
        (4, 1), (4, 2), 
        (1, 4), (2, 4), (3, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4),
        (1, 5), (2, 5), (5, 5), (6, 5), (7, 5),
        ]
    fill_blocks_with_image(world_grid, picB, coords_normal_road)


    # picC = grass
    coords_grass = [(5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3)]
    fill_blocks_with_image(world_grid, picC, coords_grass)

    

def fill_blocks_with_image(world_grid, image, coords):
    """Fill multiple blocks with the same image."""
    for coord in coords:
        world_grid.add_image(image, coord)





# Main loop
def main():
    clock = pygame.time.Clock()
    world_grid = World_Grid(screen)

    # Load and add images to the grid using the separate function
    load_and_add_images(world_grid)

    running = True

    while running:
        screen.fill(BROWN)
        world_grid.draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        pygame.display.flip()
        clock.tick(60)

    pygame.quit()




if __name__ == "__main__":
    main()
