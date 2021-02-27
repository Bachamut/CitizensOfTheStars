import pygame

def check_events():


    for event in pygame.event.get():
        # loop exit
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # fire_bullet mechanics
            if event.key == pygame.K_w:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            # changing decouple status for stop mechanics
            if event.key == pygame.K_SPACE:
                active = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                active = False