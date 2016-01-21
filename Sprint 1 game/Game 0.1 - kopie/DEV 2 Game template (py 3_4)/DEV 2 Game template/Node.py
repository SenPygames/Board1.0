print("Welcome sir")
import pygame
import sys
import os
from time import*
from Car import*
from pygame.locals import *
from win32api import GetSystemMetrics

print ("Width =", GetSystemMetrics(0))
print ("Height =", GetSystemMetrics(1))

#window size
pygame.init()
size = width, height = GetSystemMetrics(0),GetSystemMetrics(1)
screen = pygame.display.set_mode(size)
offset = 50
board_size = 10
pygame.display.set_caption('boobies')




#assets
if size == (1600, 900):
    Wallpaper = pygame.image.load("MenuWallpaper900p.png")
if size == (1920, 1080):
    Wallpaper = pygame.image.load("MenWallpaper1080p.png")
if size == (1366,768):
    Wallpaper = pygame.image.load("MenuWallpaper1366p.png")
QuitButton = pygame.image.load("QuitButton.png")
StartButton = pygame.image.load("StartButton.png")
if size == (1600, 900):
    Board = pygame.image.load("BoardGame900p.png")
if size == (1920, 1080):
    Board = pygame.image.load("BoardGame1080p.png")


#Music
#music
pygame.mixer.init()
pygame.mixer.music.load("TitleMusic.mp3")
pygame.mixer.music.play()

clock = pygame.time.Clock()
time = clock

#wallpaper logic
def wall(xw,yw):
    screen.blit(Wallpaper,(xw,yw))

#QuitButton logic
def Quit(xq,yq):
    screen.blit(QuitButton,(xq,yq))

#StartButton logic
def start(xs,ys):
    screen.blit(StartButton,(xs,ys))



#testboard logic
def board(xb,yb):
    screen.blit(StartButton, (xb,yb))

#hierdoor blijft t beeld staan for some reason + Fullscreen
def CornerTile(x,y):
    x = (0)
    y = (0)
    gameDisplay.blit(boardgame,(x,y))

def Player1Glove(List):
    x = PlayerList1.Position_X
    y = PlayerList1.Position_Y
    gameDisplay.blit(Player1,(x,y))

DISPLAYSURF = pygame.display.set_mode((0,0),FULLSCREEN)
gameExit = True
crashed = False
while not crashed:
    xs = (width * 0.6)
    ys = (height * 0.4)
    xq = (width * 0.6)
    yq = (height * 0.6)
    xw = (width * 0)
    yw= (height * 0)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = False
                crashed = True
        if event.type == pygame.QUIT:
            crashed = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            crashed = True

    else:
        if crashed == False:
            start(xs,ys)
            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    mousex, mousey = pygame.mouse.get_pos()
            if size == (1920,1080):
                if event.type == MOUSEBUTTONUP and mousex > 1152 and mousex < 1552  and mousey > 648 and mousey < 798:
                    sys.exit()
                if event.type == MOUSEBUTTONUP and mousex > 1152 and mousex < 1552  and mousey > 432 and mousey < 582:
                         screen.blit(Board (xb,yb))
            if size == (1600, 900):
                if event.type == MOUSEBUTTONUP and mousex > 960 and mousex < 1360  and mousey > 540 and mousey < 690:
                    sys.exit()
                if event.type == MOUSEBUTTONUP and mousex > 960 and mousex < 1360  and mousey > 360 and mousey < 510:
                         screen.blit(Board (xb,yb))
            if size == (1366, 768):
                if event.type == MOUSEBUTTONUP and mousex > 960 and mousex < 1360  and mousey > 540 and mousey < 690:
                    sys.exit()
                if event.type == MOUSEBUTTONUP and mousex > 960 and mousex < 1360  and mousey > 360 and mousey < 510:
                         screen.blit(Board (xb,yb))
            pygame.display.update()

            wall(xw,yw)
            Quit(xq,yq)
    clock.tick(60)


while not gameExit:
    display_width = 600
    display_height = 800
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    boardgame = pygame.image.load ("Board.png")
    gameDisplay = pygame.display.set_mode((display_height,display_width))
    pygame.display.set_caption('Surivor')
    Player1 = pygame.image.load("BoksHandschoen.png")
    board = boardgame.convert()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.key == pygame.K_2:
                PlayerList1 = PlayerList1.tail
    if PlayerList1.Name == "Pos41":
        PlayerList1 = PlayerPosList1
    gameDisplay.fill(white)
    CornerTile(0,0)
    Player1Glove(PlayerList1)
    pygame.display.flip()

pygame.quit()
quit()


