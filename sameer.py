import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sameer Car Racing Game")

# Load images
car_image = pygame.image.load("car.png")
car_rect = car_image.get_rect()
car_rect.midbottom = (WIDTH // 2, HEIGHT - 20)

obstacle_image = pygame.image.load("obstacle.png")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Variables
car_speed = 5
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.left > 0:
        car_rect.x -= car_speed
    if keys[pygame.K_RIGHT] and car_rect.right < WIDTH:
        car_rect.x += car_speed

    # Move obstacles
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_rect = obstacle_image.get_rect()
        obstacle_rect.midtop = (random.randint(0, WIDTH - obstacle_rect.width), 0)
        obstacles.append(obstacle_rect)

    for obstacle_rect in obstacles:
        obstacle_rect.y += obstacle_speed
        if obstacle_rect.colliderect(car_rect):
            pygame.quit()
            sys.exit()

    # Remove obstacles that are off the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]

    # Update score
    score += 1

    # Draw everything
    screen.fill(BLACK)
    screen.blit(car_image, car_rect)
    for obstacle_rect in obstacles:
        screen.blit(obstacle_image, obstacle_rect)

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)
