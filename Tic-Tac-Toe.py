# TicTacToe Game
import random
# This visualises the board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def playerCharacter():
    Choice = ''
    while not (Choice == 'X' or Choice == 'O'):
        print('Please choose either X or O as your character')
        Choice = input().upper()

    if Choice == 'X':
        return ['O', 'X']
    else:
        return ['X', 'O']

def goesFirst():
    if random.randint(0,1) == 0:
        return 'Computer'
    else:
        return 'Player'
    
def makeAMove(board, character):
    print('Please enter a move from one of these options:')
    print('top-L, top-M, top-R;')
    print('mid-L, mid-M, mid-R;')
    print('low-L, low-M, low-R')
    playerMove = input()
    if playerMove[4] in ('l', 'm', 'r'):
        playerMove = playerMove[:4] + playerMove[4].capitalize()
    if playerMove in board:
          if board[playerMove] == ' ':
              board[playerMove] = character
              return True
          else:
              print('Invalid Move, that space is occupied please try another.')
              return False
    else:
        print('Please choose a valid move from the above list.')
        return False

def isGameWon(board, letter):
    return (board['top-L'] == letter and board['top-M'] == letter and board['top-R'] == letter) or \
    (board['mid-L'] == letter and board['mid-M'] == letter and board['mid-R'] == letter) or \
    (board['low-L'] == letter and board['low-M'] == letter and board['low-R'] == letter) or \
    (board['top-L'] == letter and board['mid-L'] == letter and board['low-L'] == letter) or \
    (board['top-M'] == letter and board['mid-M'] == letter and board['low-M'] == letter) or \
    (board['top-R'] == letter and board['mid-R'] == letter and board['low-R'] == letter) or \
    (board['top-L'] == letter and board['mid-M'] == letter and board['low-R'] == letter) or \
    (board['top-R'] == letter and board['mid-M'] == letter and board['low-L'] == letter) 
    
def isBoardFull(board):
    return ' ' not in board.values()

def computersTurn(board, letter):
    boardCopy = board.copy()
    boardCopyCorners = {spaces:board[spaces] for spaces in ['top-L','top-R','low-L','low-R']}
    if letter == 'X':
        opLetter = 'O'
    else:
        opLetter = 'X'
#first look for winning moves
    for moves in boardCopy.keys():
        if boardCopy[moves] == ' ':
            boardCopy[moves] = letter
            if isGameWon(boardCopy, letter) == True:
                board[moves] = letter
                return
            else:
                boardCopy[moves] = ' '
    #Next most strategic move - stop an opponent win
    for moves in boardCopy.keys():
        if boardCopy[moves] == ' ':
            boardCopy[moves] = opLetter
            if isGameWon(boardCopy, opLetter) == True:
                board[moves] = letter
                return
            else:
                boardCopy[moves] = ' '
    if ' ' in boardCopyCorners.values():
        for corners in boardCopyCorners.keys():
            if boardCopyCorners[corners] == ' ':
                board[corners] = letter
                return
    elif boardCopy['mid-M'] == ' ':
        board['mid-M'] = letter
        return
    else:
        for moves in boardCopy.keys():
            if boardCopy[moves] == ' ':
                board[moves] = letter
                return

            


# This assigns the positions to a dictionary

playAgain = True
while playAgain == True:
    theBoard = {'top-L': ' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}
    print('Hello and Welcome to Tic Tac Toe!')
    print('Do you want to be X or O?')
    playerComputer = playerCharacter()

    turn = goesFirst()
    print('The ' + turn + ' will go first.')
    gameWon = False
    boardFull = False
    while gameWon == False and boardFull == False:
        if turn == 'Player':
            validMove = False
            printBoard(theBoard)
            while validMove == False:
                try:
                    validMove = makeAMove(theBoard, playerComputer[1]) 
                except:
                    print('Please make a valid move from the above list')
            gameWon = isGameWon(theBoard, playerComputer[1])
            if gameWon == True:
                winner = 'Player'
            boardFull = isBoardFull(theBoard)
            turn = 'Computer'

        else:
            computersTurn(theBoard,playerComputer[0])
            gameWon = isGameWon(theBoard, playerComputer[0])
            if gameWon == True:
                winner = 'Computer'
            boardFull = isBoardFull(theBoard)
            turn = 'Player'

        print('DEBUG: ' + str(gameWon) + str(boardFull))

    printBoard(theBoard)
    if gameWon == True:
        if winner == 'Player':
            print('Congratulations, you\'ve beaten the computer!!')
        else:
            print('Oooh unlucky, you\'ll get it next time!')
    elif boardFull == True:
        print('Looks like that\'s a draw! Let\'s have another go.')
        
    while True:
        print('Would you like to play again? (Y/N)')
        replay = input().upper()
        if replay[0] == 'Y':
            playAgain = True
            break
        elif replay[0] == 'N':
            playAgain = False
            break
    

