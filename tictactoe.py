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
    if num1 == 1:
        if square1 == 'X' or square1 == 'O':
            return False
        else:
            return True
    if num1 == 2:
        if square2 == 'X' or square2 == 'O':
            return False
        else:
            return True
    if num1 == 3:
        if square3 == 'X' or square3 == 'O':
            return False
        else:
            return True
    if num1 == 4:
        if square4 == 'X' or square4 == 'O':
            return False
        else:
            return True
    if num1 == 5:
        if square5 == 'X' or square5 == 'O':
            return False
        else:
            return True
    if num1 == 6:
        if square6 == 'X' or square6 == 'O':
            return False
        else:
            return True
    if num1 == 7:
        if square7 == 'X' or square7 == 'O':
            return False
        else:
            return True
    if num1 == 8:
        if square8 == 'X' or square8 == 'O':
            return False
        else:
            return True
    if num1 == 9:
        if square9 == 'X' or square9 == 'O':
            return False
        else:
            return True
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
        while isempty(turn) == False:
            turn = int(input('Where would you like to go?: '))
        if turn == 1:
            isempty(turn)
            square1 = 'X'
            printboard()
        elif turn == 2:
            isempty(turn)
            square2 = 'X'
            printboard()
        elif turn == 3:
            isempty(turn)
            square3 = 'X'
            printboard()
        elif turn == 4:
            isempty(turn)
            square4 = 'X'
            printboard()
        elif turn == 5:
            isempty(turn)
            square5 = 'X'
            printboard()
        elif turn == 6:
            isempty(turn)
            square6 = 'X'
            printboard()
        elif turn == 7:
            isempty(turn)
            square7 = 'X'
            printboard()
        elif turn == 8:
            isempty(turn)
            square8 = 'X'
            printboard()
        elif turn == 9:
            isempty(turn)
            square9 = 'X'
            printboard()
    