from GameObjects.Unit import GameObject
from Variables import *
import pygame
class Player(GameObject):
    def __init__(self,rect,Health):
        super().__init__(rect)
        self.velocity = 3
        self.Health = Health
        self.MaxHealth = Health

    def MoveRight(self):
        self.rect.x += self.velocity

    def MoveLeft(self):
        self.rect.x -= self.velocity

    def Draw(self,screen,color):
        self.render(screen, color)
        if self.rect.x+int(PLAYERLENGTH) > 1000 and self.rect.x+int(PLAYERLENGTH) < 1000+int(PLAYERLENGTH):
            pygame.draw.rect(screen,color,(self.rect.x-1000,self.rect.y,PLAYERLENGTH,PLAYERLENGTH))
        elif self.rect.x+int(PLAYERLENGTH) >= 1000+int(PLAYERLENGTH):
            self.rect.x -= 1000

        if self.rect.x-int(PLAYERLENGTH) < 0 and self.rect.x-int(PLAYERLENGTH) > -int(PLAYERLENGTH):
            pygame.draw.rect(screen,color,(self.rect.x+1000,self.rect.y,PLAYERLENGTH,PLAYERLENGTH))
        elif self.rect.x-int(PLAYERLENGTH) < -int(PLAYERLENGTH):
            self.rect.x += 1000

    def GetHit(self,Bullet):
        if self.rect.colliderect(Bullet.rect) == True:
            self.Health -= 1

