import pygame

# initialize of pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("CitizensOfTheStars")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen background color (RBG)
    screen.fill((50, 80, 000))

    pygame.display.update()