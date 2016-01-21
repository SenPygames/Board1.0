import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *
from Car import *

pygame.init()
display_width = 1000
display_height = 1400
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
boardgame = pygame.image.load ("Board.png")
gameDisplay = pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('Surivor')
Player1 = pygame.image.load("BoksHandschoen.png")
screen = pygame.display.set_mode(boardgame.get_rect().size,0,32)

board = boardgame.convert() # now you can convert

def CornerTile(x,y):
    x = (0)
    y = (0)
    gameDisplay.blit(boardgame,(x,y))

def Player1Glove(List):
    x = PlayerList1.Position_X
    y = PlayerList1.Position_Y
    gameDisplay.blit(Player1,(x,y))



while not gameExit:
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
    print (PlayerList1.Name)
    pygame.display.flip()

pygame.quit()
quit()