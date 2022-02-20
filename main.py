from GameObjects.Player import Player
from GameObjects.Bullet import Bullet
from Machines.BulletMachine import BulletMachine
from Machines.WaveMachine import WaveMachine
from GameObjects.Invader import Invader
from Machines.MovementMachine import MovementMachine
from Variables import *
from MiscFunctions.Scores import Scores
from GameObjects.Shooter.Shooter import Shooter
from Machines.ShooterMachine import ShooterMachine
from MiscFunctions.HealthCounter import PlayerHealthCounter,BossHealthCounter
import pygame,sys

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('GTA6 Precolumbian Build')
myfont = pygame.font.SysFont('Comic Sans MS', 50)
GameOverFont = pygame.font.SysFont('Comic Sans MS', 100)

Player1 = Player(pygame.Rect(300,650,PLAYERLENGTH,PLAYERLENGTH),100)

while True:
    #print("penis") #very imporatant - dont remove
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN and GameOver == False:
            if event.key == pygame.K_SPACE:
                BulletDex.append(Bullet(pygame.Rect(Player1.rect.x + 12, Player1.rect.y - 15, 5, 15)))
                BulletCount += 1
    if GameOver == False:
        screen.fill(white)
        if MovementMachine(Player1) == True:
            GameOver = True

        PlayerHealthCounter(screen, Player1)
        for i in range(len(ShooterDex)):
            BossHealthCounter(screen, ShooterDex[i],i+1)

        WaveDex, Score, BulletDex = WaveMachine(WaveDex,screen,black,Score,BulletDex,Player1)
        ShooterBulletDex, HealthBoxDex = ShooterMachine(ShooterDex, screen, red, Player1, ShooterBulletDex,HealthBoxDex)

        for i in ShooterDex:
            Score = i.Scoring(BulletDex, Score)
            ShooterDex,BulletDex,HealthBoxDex = i.HitDetect(BulletDex,ShooterDex,HealthBoxDex)

        if Wave_Time % WaveOffTime == 0:
            ShooterDex.append(Shooter(pygame.Rect(0, 0, INVADERLENGTH, INVADERLENGTH),BossHealth))
            if WaveOffTime > 300:
                WaveOffTime -= 50
            BossHealth += 2
        elif Wave_Time % 150 == 0:
            WaveDex.append(Invader(pygame.Rect(0,0,INVADERLENGTH,INVADERLENGTH)))

        Wave_Time += 1
        Player1.Draw(screen,blue)
        BulletDex = BulletMachine(BulletDex, screen, black)
        BulletMachine(ShooterBulletDex,screen,black)
        Scores(screen, BulletCount, Score, myfont, red,GameOver,GameOverFont)
        pygame.display.update()
        clock.tick(120)