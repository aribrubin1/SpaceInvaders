from GameObjects.Unit import GameObject
class HealthBox(GameObject):
    def __init__(self,rect,HealthAmount):
        super().__init__(rect)
        self.HealthAmount = HealthAmount

    def Fall(self,HealthBoxDex):
        self.rect.y += 1
        if self.rect.y > 1000:
            HealthBoxDex.remove(self)
        return HealthBoxDex

    def Collect(self,Player,HealthBoxDex):
        if self.rect.colliderect(Player.rect) == True:
            if Player.Health + self.HealthAmount > Player.MaxHealth:
                Player.Health = Player.MaxHealth
            else:
                Player.Health += self.HealthAmount
            HealthBoxDex.remove(self)
        return HealthBoxDex
