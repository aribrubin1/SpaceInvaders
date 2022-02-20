def WaveMachine(WaveDex,screen,color,Score,BulletDex,Player):
    CopyDex = list(WaveDex)
    for i in WaveDex:
        i.render(screen, color)
        i.Move()
        if i.Down == True:
            if i.Movedown() == False:
                i.DownCount = 0
            else:
                i.DownCount += 1

        Score = i.Scoring(BulletDex, Score)
        CopyDex, BulletDex = i.HitDetect(BulletDex, WaveDex)
        if i.HitPlayer(Player) == True:
            CopyDex.remove(i)
            Player.Health -= 5

    return CopyDex,Score,BulletDex