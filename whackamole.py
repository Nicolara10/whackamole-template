import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        # Grid and Mole Setup
        grid_size = 32
        mole_x, mole_y = 0, 0  # Initial mole position

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get mouse position
                    mouse_x, mouse_y = event.pos
                    # Check if the mole is clicked
                    if mole_x <= mouse_x < mole_x + grid_size and mole_y <= mouse_y < mole_y + grid_size:
                        # Move mole to a new random grid square
                        mole_x = random.randrange(0, 640, grid_size)
                        mole_y = random.randrange(0, 512, grid_size)

            screen.fill("light green")

            # Draw the grid
            for x in range(0, 640, grid_size):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0, 512, grid_size):
                pygame.draw.line(screen, "black", (0, y), (640, y))

            # Draw the mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
