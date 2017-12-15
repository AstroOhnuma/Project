#Astro Ohnuma
#12/14/17
#conwaysgameoflife.py - Mathematical model of life and population growth
from ggame import *

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

def buildboard():
    for row in range(0,10):
        for col in range(0,10):
            print(board[row][col],' ',end = '')
        print()
def redrawall():
    for item in App().spritelist[:]:
        item.destroy()
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    blackoutline = LineStyle(1,black)
    whiteoutline = LineStyle(1,white)
    deadcell = RectangleAsset(20,20,blackoutline,white)
    livingcell = RectangleAsset(20,20,whiteoutline,black)
    for row in range(0,10):
        for col in range(0,10):
            Sprite(deadcell)
redrawall()
App().run()