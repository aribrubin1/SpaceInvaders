from GameObjects.Unit import GameObject
from Variables import InvaderDropLength
from Variables import Score

class Invader(GameObject):
    def __init__(self,rect):
        super().__init__(rect)
        self.MovementState = "RIGHT"
        self.Down = False
        self.DownCount = 0

    def Move(self):
        if self.MovementState == "RIGHT" and self.Down == False:
            self.rect.x += 2
        elif self.MovementState == "LEFT" and self.Down == False:
            self.rect.x -= 2

        if self.MovementState == "RIGHT" and self.rect.x > 900:
            self.MovementState = "LEFT"
            self.Down = True

        if self.MovementState == "LEFT" and self.rect.x < 100:
            self.MovementState = "RIGHT"
            self.Down = True

    def Movedown(self):
        if self.DownCount == InvaderDropLength:
            self.Down = False
            return False
        else:
            self.rect.y += 3

    def Scoring(self,BulletDex,Score):
        for i in BulletDex:
            if self.rect.colliderect(i.rect) == True:
                Score += 1
        return Score

    def HitDetect(self,BulletDex,WaveDex):
        TempDex = list(BulletDex)
        for i in BulletDex:
            if self.rect.colliderect(i.rect) == True:
                WaveDex.remove(self)
                TempDex.remove(i)
        return WaveDex,TempDex

    def HitPlayer(self,Player):
        if self.rect.colliderect(Player.rect) == True:
            return True