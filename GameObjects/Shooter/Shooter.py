from GameObjects.Invader import Invader
from GameObjects.Shooter.ShooterBullet import ShooterBullet
from GameObjects.HealthBox import HealthBox
from Variables import ShooterRange
import pygame
class Shooter(Invader):
    def __init__(self,rect,Health):
        super().__init__(rect)
        self.MovementState = "RIGHT"
        self.Down = False
        self.Health = Health
        self.MaxHealth = Health

    def Shoot(self,BulletDex):
        BulletDex.append(ShooterBullet(pygame.Rect(self.rect.x + 12,self.rect.y + 15,5,15)))
        return BulletDex

    def Aim(self,Player,BulletDex):
        if self.rect.x > Player.rect.x-ShooterRange and self.rect.x < Player.rect.x+ShooterRange:
            self.Shoot(BulletDex)
        else:
            return BulletDex

    def HitDetect(self,BulletDex,WaveDex,HealthBoxDex):
        TempBullet = list(BulletDex)
        for i in BulletDex:
            if self.rect.colliderect(i.rect) == True:
                TempBullet.remove(i)
                if self.Health > 0:
                    self.Health -= 5
                else:
                    HealthBoxDex.append(HealthBox(pygame.Rect(self.rect.x,self.rect.y,15,15),self.MaxHealth/2))
                    WaveDex.remove(self)
        return WaveDex,TempBullet,HealthBoxDex