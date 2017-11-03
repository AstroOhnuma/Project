#Astro Ohnuma
#11/1/17
#tictactoe.py - first project, tictactoe without graphics
from random import randint
win = 0
player = 'none'
com = 'also none'
square1 = 1
square2 = 2
square3 = 3
square4 = 4
square5 = 5
square6 = 6
square7 = 7
square8 = 8
square9 = 9
x = 'X'
o = 'O'
def printboard():
    print(' ---','---','---')
    print('|',square1,'|',square2,'|',square3,'|')
    print(' ---','---','---')
    print('|',square4,'|',square5,'|',square6,'|')
    print(' ---','---','---')
    print('|',square7,'|',square8,'|',square9,'|')
    print(' ---','---','---')
def isempty(num1):
    if num1 == x or num1 == o:
        return True
    else:
        return False
def winner():
    if win == 1:
        return True
    else:
        return False
def fullboard():
    if sqaure1 == x or square1 == o and sqaure2 == x or square2 == o and sqaure3 == x or square3 == o and sqaure4 == x or square4 == o and sqaure5 == x or square5 == o and sqaure6 == x or square6 == o and sqaure7 == x or square7 == o and sqaure8 == x or square8 == o and sqaure9 == x or square9 == o:
        return True
    else:
        return False
if __name__ == '__main__':
    '''
    first = randint(1,2)
    if first == 1:
        print('Player goes first!')
    else:
        print('Computer goes first!')
    choice = input('Would you like to be Xs or Os?')
    if choice == 'x' or choice == 'X':
        player = x
        com = o
    elif choice == 'o' or choice == 'O':
        player = o
        com = x'''
    printboard()
    while win < 1:
        turn = int(input('Where would you like to go?: '))
        if turn == 1:
            square1 = 'X'
            printboard()
        elif turn == 2:
            square2 = 'X'
            printboard()
        elif turn == 3:
            square3 = 'X'
            printboard()
        elif turn == 4:
            square4 = 'X'
            printboard()
        elif turn == 5:
            square5 = 'X'
            printboard()
        elif turn == 6:
            square6 = 'X'
            printboard()
        elif turn == 7:
            square7 = 'X'
            printboard()
        elif turn == 8:
            square8 = 'X'
            printboard()
        elif turn == 9:
            square9 = 'X'
            printboard()
        fullboard()
    