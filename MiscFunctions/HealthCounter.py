import pygame
def PlayerHealthCounter(screen,entity):
    white = [255, 255, 255]
    black = (0, 0, 0)
    blue = (0, 0, 255)
    pygame.draw.rect(screen,black,(200,700,520,60))
    pygame.draw.rect(screen, white, (210, 710, 500, 40))
    Percentage = entity.Health / entity.MaxHealth
    Leng = int(Percentage * 500)

    pygame.draw.rect(screen, blue, (210, 710, Leng, 40))

def BossHealthCounter(screen,entity,preset):
    white = [255, 255, 255]
    black = (0, 0, 0)
    red = (255, 0, 0)

    Percentage = entity.Health / entity.MaxHealth
    Leng = int(Percentage * 120)
    PhaseShift = 120 - Leng
    if preset == 1:
        pygame.draw.rect(screen, black, (940, 500, 25, 130))
        pygame.draw.rect(screen, white, (945, 505, 15, 120))
        pygame.draw.rect(screen, red, (945, 505+PhaseShift, 15, Leng))
    elif preset == 2:
        pygame.draw.rect(screen, black, (940, 500-200, 25, 130))
        pygame.draw.rect(screen, white, (945, 505-200, 15, 120))
        pygame.draw.rect(screen, red, (945, 505-200 + PhaseShift, 15, Leng))
    elif preset == 3:
        pygame.draw.rect(screen, black, (940, 500-200-200, 25, 130))
        pygame.draw.rect(screen, white, (945, 505-200-200, 15, 120))
        pygame.draw.rect(screen, red, (945, 505-200-200 + PhaseShift, 15, Leng))