print("Welcome sir")
import pygame
import sys
import os
from time import*
from pygame.locals import *
from Assets import *
from win32api import GetSystemMetrics

print ("Width =", GetSystemMetrics(0))
print ("Height =", GetSystemMetrics(1))



#window size
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

pygame.init()

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

xw = (width * 0)
yw= (height * 0)

#QuitButton logic
def quit(xq,yq):
    screen.blit(QuitButton,(xq,yq))

xq = (width * 0.6)
yq = (height * 0.6)

#StartButton logic
def start(xs,ys):
    screen.blit(StartButton,(xs,ys))

xs = (width * 0.6)
ys = (height * 0.4)

#testboard logic
def board(xb,yb):
    screen.blit(StartButton, (xb,yb))



#hierdoor blijft t beeld staan for some reason + Fullscreen
crashed = False
DISPLAYSURF = pygame.display.set_mode((0,0),FULLSCREEN)

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

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
            quit(xq,yq)
    clock.tick(60)


