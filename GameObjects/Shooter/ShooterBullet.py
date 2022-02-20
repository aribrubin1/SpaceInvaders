from GameObjects.Bullet import Bullet
class ShooterBullet(Bullet):
    def __init__(self,rect):
        super().__init__(rect)
        self.velocity = 7

    def advance(self):
        self.rect.y += self.velocity
        self.velocity += 0.2

    def Remove(self,BulletDex):
        if self.rect.y > 1000:
            BulletDex.remove(self)