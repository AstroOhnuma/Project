#Astro Ohnuma
#12/14/17
#conwaysgameoflife.py - Mathematical model of life and population growth
from ggame import *

def buildboard():
    return data['board']
def redrawall():
    for item in App().spritelist[:]:
        item.destroy()
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    blackoutline = LineStyle(1,black)
    whiteoutline = LineStyle(1,white)
    deadcell = RectangleAsset(30,30,blackoutline,white)
    livingcell = RectangleAsset(30,30,whiteoutline,black)
    nextgenbox = RectangleAsset(150,60,blackoutline,black)
    notnext = TextAsset('Next',fill=white,style='bold 30pt Times')
    gen = TextAsset('Generation',fill=white,style='bold 30pt Times')
    Sprite(nextgenbox, (0,300))
    Sprite(nextgenbox, (150,300))
    Sprite(notnext, (0,310))
    Sprite(gen, (100,310))
    for row in range(0,10):
        for col in range(0,10):
            Sprite(deadcell, (col*30,row*30))
            if data['board'][row][col] == 1:
                Sprite(livingcell, (col*30,row*30))
            else:
                Sprite(deadcell, (col*30,row*30))
def numneighbors(num1,num2):
    count = 0
    if num1 > 0 and num2 > 0 and data['board'][num1-1][num2-1] == 1:
        count += 1
    if num1 > 0 and data['board'][num1-1][num2] == 1:
        count += 1
    if num1 > 0 and num2 < 9 and data['board'][num1-1][num2+1] == 1:
        count += 1
    if num2 < 9 and data['board'][num1][num2+1] == 1:
        count += 1
    if num1 < 9 and num2 < 9 and data['board'][num1+1][num2+1] == 1:
        count += 1
    if num1 <9 and data['board'][num1+1][num2] == 1:
        count += 1
    if num1 < 9 and num2 > 0 and data['board'][num1+1][num2-1] == 1:
        count += 1
    if num2 > 0 and data['board'][num1][num2-1] == 1:
        count += 1
    return count
def nextgeneration():
    newboard = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    for row in range(0,10):
        for col in range(0,10):
            num = numneighbors(row,col)
            if data['board'][row][col]==1 and num < 2:
                newboard[row][col] = 0
            elif data['board'][row][col]==1 and num > 3:
                newboard[row][col] = 0
            elif data['board'][row][col]==1 and num == 2 or data['board'][row][col]==1 and num == 3:
                newboard[row][col] = 1
            elif data['board'][row][col]==0 and num == 3:
                newboard[row][col] = 1
    data['board'] = newboard
    redrawall()
def mouseclick(event):
        if event.y//30 > 9 or event.x//30 > 9:
            nextgeneration()
        else:
            data['board'][event.y//30][event.x//30] = 1
            print('You clicked row',int(event.y/30),'and column',int(event.x/30))
            redrawall()
if __name__ == '__main__':
    data = {}
    data['board'] = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    buildboard()
    redrawall()
    
    App().listenMouseEvent('click', mouseclick)
    App().run()