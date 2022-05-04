import pygame

# Constants

# Screen dimensions
WIDTH = 640
HEIGHT = 480

# Game speed
FPS = 60


# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
RED1 = (255, 100, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# GAME Constants
SIZE = 10

def main():
    # Game init
    pygame.init()

    x = 100
    y = 100
    x_step = 0
    y_step = 0

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Your Game Name')

    clock = pygame.time.Clock()

    running = True

    # Game loop
    while running:
        # 1. Process input/event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LEFT:
                    x_step -= 2
                    y_step = 0
                if event.type == pygame.K_RIGHT:
                    x_step = 2
                    y_step = 0
                if event.type == pygame.K_UP:
                    y_step -= 2
                    x_step = 0
                if event.type == pygame.K_DOWN:
                    y_step = 2
                    x_step = 0
        # 2. Update objects
        x += x_step
        y += y_step


        if x <= 0 or x + SIZE  >= WIDTH:
            x_step = 0

        if y <= 0 or y + SIZE >= HEIGHT:
            y_step = 0
        # 3. Draw objects
        # Clear screen
        screen.fill(BLACK)
        x += x_step
        y += y_step


        pygame.draw.rect(screen, RED, pygame.Rect(x, y, SIZE, SIZE), 2)
        pygame.draw.rect(screen, RED1, pygame.Rect(x+2, y+2, SIZE-4, SIZE-4), 2)

        # 4. sync time
        clock.tick(FPS)

        pygame.display.flip()



if name == 'main':
    main()