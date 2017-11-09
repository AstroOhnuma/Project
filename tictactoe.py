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
    elif num1 == 2:
        if square2 == 'X' or square2 == 'O':
            return False
        else:
            return True
    elif num1 == 3:
        if square3 == 'X' or square3 == 'O':
            return False
        else:
            return True
    elif num1 == 4:
        if square4 == 'X' or square4 == 'O':
            return False
        else:
            return True
    elif num1 == 5:
        if square5 == 'X' or square5 == 'O':
            return False
        else:
            return True
    elif num1 == 6:
        if square6 == 'X' or square6 == 'O':
            return False
        else:
            return True
    elif num1 == 7:
        if square7 == 'X' or square7 == 'O':
            return False
        else:
            return True
    elif num1 == 8:
        if square8 == 'X' or square8 == 'O':
            return False
        else:
            return True
    elif num1 == 9:
        if square9 == 'X' or square9 == 'O':
            return False
        else:
            return True
def winner():
    if isempty(1) == False and isempty(2) == False and isempty(3) == False:
        return True
    else:
        return False
    if isempty(4) == False and isempty(5) == False and isempty(6) == False:
        return True
    else:
        return False
    if isempty(7) == False and isempty(8) == False and isempty(9) == False:
        return True
    else:
        return False
    if isempty(1) == False and isempty(5) == False and isempty(9) == False:
        return True
    else:
        return False
    if isempty(3) == False and isempty(5) == False and isempty(7) == False:
        return True
    else:
        return False
    if isempty(1) == False and isempty(4) == False and isempty(7) == False:
        return True
    else:
        return False
    if isempty(2) == False and isempty(5) == False and isempty(8) == False:
        return True
    else:
        return False
    if isempty(3) == False and isempty(6) == False and isempty(9) == False:
        return True
    else:
        return False
def fullboard():
    if isempty(1) == False and isempty(2) == False and isempty(3) == False and isempty(4) == False and isempty(5) == False and isempty(6) == False and isempty(7) == False and isempty(8) == False and isempty(9) == False:
        return True
    else:
        return False
if __name__ == '__main__':
    printboard()
    while win < 1:
        turn = int(input('Where would you like to go?: '))
        while isempty(turn) == False:
            turn = int(input('Where would you like to go?: '))
        if turn == 1:
            isempty(turn)
            square1 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 2:
            isempty(turn)
            square2 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 3:
            isempty(turn)
            square3 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 4:
            isempty(turn)
            square4 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 5:
            isempty(turn)
            square5 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 6:
            isempty(turn)
            square6 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 7:
            isempty(turn)
            square7 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 8:
            isempty(turn)
            square8 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 9:
            isempty(turn)
            square9 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        com = randint(1,9)
        while isempty(com) == False:
            com = randint(1,9)
        if com == 1:
            isempty(com)
            square1 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 2:
            isempty(com)
            square2 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 3:
            isempty(com)
            square3 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 4:
            isempty(com)
            square4 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 5:
            isempty(com)
            square5 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 6:
            isempty(com)
            square6 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 7:
            isempty(com)
            square7 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 8:
            isempty(com)
            square8 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 9:
            isempty(com)
            square9 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        
    