import pygame
from urllib.request import urlopen
import json


# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 500
screen_height = 500

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Fill the screen with black color
screen.fill((0, 0, 0))

# Draw a circle and annimate it to F1 data from the API
response = urlopen('https://api.openf1.org/v1/location?session_key=9161&driver_number=81&date>2023-09-16T13:03:35.200&date<2023-09-16T13:03:35.800')
data = json.loads(response.read().decode('utf-8'))
print(data)
for item in data:
    x = item["x"]
    y = item["y"]
    pygame.draw.circle(screen, (255, 255, 255), (x/10, y/10), 15, 0)

# Update the display
pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()