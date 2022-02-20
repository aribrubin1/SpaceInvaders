def BulletMachine(BulletDex,screen,color):
    for i in BulletDex:
        i.render(screen,color)
        i.advance()
        i.Remove(BulletDex)
    return BulletDex