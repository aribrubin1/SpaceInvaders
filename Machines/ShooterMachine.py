from Variables import green
def ShooterMachine(WaveDex,screen,color,Player,BulletDex,HealthBoxDex):
    for i in WaveDex:
        i.render(screen, color)
        i.Move()
        if i.Down == True:
            if i.Movedown() == False:
                i.DownCount = 0
            else:
                i.DownCount += 1

        i.Aim(Player,BulletDex)
    for i in BulletDex:
        Player.GetHit(i)
    TempHealthBoxDex = list(HealthBoxDex)
    for i in HealthBoxDex:
        i.render(screen,green)
        TempHealthBoxDex = i.Fall(HealthBoxDex)
        TempHealthBoxDex = i.Collect(Player,HealthBoxDex)
    return BulletDex,TempHealthBoxDex