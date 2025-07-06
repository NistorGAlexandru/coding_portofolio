import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 30
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Squares")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT // 2 - PLAYER_SIZE // 2, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 5

# Enemies
enemies = []

def spawn_enemy():
    x = random.randint(0, WIDTH - ENEMY_SIZE)
    y = random.randint(0, HEIGHT - ENEMY_SIZE)
    enemy = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(enemy)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed

    # Spawn enemies
    if random.random() < 0.01:
        spawn_enemy()

    # Move enemies
    for enemy in enemies:
        enemy.y += 3
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # Check for collisions
    for enemy in enemies:
        if player.colliderect(enemy):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
