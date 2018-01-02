#Astro Ohnuma
#12/14/17
#conwaysgameoflife.py - Mathematical model of life and population growth
from ggame import *

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

def buildboard():
    for row in range(0,10):
        for col in range(0,10):
            print(board[row][col],' ',end = '')
def redrawall():
    for item in App().spritelist[:]:
        item.destroy()
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    blackoutline = LineStyle(1,black)
    whiteoutline = LineStyle(1,white)
    deadcell = RectangleAsset(30,30,blackoutline,white)
    livingcell = RectangleAsset(30,30,whiteoutline,black)
    for row in range(0,10):
        for col in range(0,10):
            Sprite(deadcell, (row*30,col*30))
def numneighbors(num1,num2):
    count = 0
    if board[num1-2][num2-1] == 1:
        count += 1
    if board[num1-1][num2-2] == 1:
        count += 1
    if board[num1][num2-1] == 1:
        count += 1
    if board[num1-1][num2] == 1:
        count += 1
    if board[num1][num2-2] == 1:
        count += 1
    if board[num1-2][num2] == 1:
        count += 1
    if board[num1][num2] == 1:
        count += 1
    if board[num1-2][num2-2] == 1:
        count += 1
def nextgeneration():
    for row in range(0,10):
        for col in range(0,10):
            print(board[row][col],' ',end = '')
def mouseclick(event):
        print('You clicked row',event.y/30,'and column',event.x/30)
if __name__ == '__main__':
    buildboard()
    redrawall()
    
    App().listenMouseEvent('click', mouseclick)
    App().run()