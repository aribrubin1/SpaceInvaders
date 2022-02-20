from GameObjects.Unit import GameObject
class Bullet(GameObject):
    def __init__(self,rect):
        super().__init__(rect)
        self.velocity = 7

    def advance(self):
        self.rect.y -= self.velocity
        self.velocity += 0.2

    def Remove(self,BulletDex):
        if self.rect.y < 0:
            BulletDex.remove(self)
