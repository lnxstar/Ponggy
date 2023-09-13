import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Ball properties
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5
ball_speed_y = 5

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce the ball off the edges
    if ball_x < 0 or ball_x > screen_width - ball_radius * 2:
        ball_speed_x *= -1
    if ball_y < 0 or ball_y > screen_height - ball_radius * 2:
        ball_speed_y *= -1

    # Fill the screen with black
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
