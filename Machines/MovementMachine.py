import pygame
def MovementMachine(Player):
    if Player.Health <= 0:
        return True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Player.MoveRight()
        if Player.velocity < 5:
            Player.velocity += 0.05
    elif keys[pygame.K_LEFT]:
        Player.MoveLeft()
        if Player.velocity < 5:
            Player.velocity += 0.05
    else:
        Player.velocity = 3
