def Scores(screen,BulletCount,Score,myfont,color,GameOver,GameOverFont):
    ScoreCard = myfont.render(str(Score), False, color)
    if BulletCount != 0:
        Percent = str(int((Score / BulletCount)*100)) + "%"
        HitPercent = myfont.render(Percent,False,color)
    else:
        HitPercent = myfont.render("0%",False,color)

    screen.blit(ScoreCard, (800, 690))
    screen.blit(HitPercent,(20, 690))
    GAMEOVER = GameOverFont.render("GAME OVER", False, color)
    if GameOver == True:
        screen.blit(GAMEOVER,(200,200))
