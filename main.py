from audioop import mul
from ipaddress import collapse_addresses
from nis import cat
from random import randrange

board = []
playingSinglePlayer = False
player1Turn = True #Player 1 is always O's

def main():
    print("Welcome to Tic-Tac-Toe")

    mode = input("Please choose a game mode: \n(0) Single Player \n(1) Multiplayer \n")
    while (True):
        try: 
            modeInt = int(mode)
            if ((modeInt > 1) or (modeInt < 0)):
                mode = input("Please enter a valid option:")
            else:    
                break
        except: 
            mode = input("Please enter a valid option:")
            continue

    if (modeInt == 0):
        singlePlayerMode()
    elif (modeInt == 1):
        multiPlayerMode()

def singlePlayerMode():
    '''Starts a single player game against the computer'''
    global playingSinglePlayer
    playingSinglePlayer = True
    global player1Turn
    initializeGrid()
    printGrid(board)

    while (checkWin() is False):
        if player1Turn is True:
            location = input("It is your turn! Pick a move:")
            while playMove(location) is False:
                location = input("Invalid move. Please pick a different move:")
            printGrid(board)
            print()
            player1Turn = False
        else:
            computerTurn()
            player1Turn = True


def multiPlayerMode():
    '''Starts a multiplayer game between two opponents'''
    playingSinglePlayer = False
    print("Welcome to multiplayer")

def playMove(location):

    row = int(location) // 3
    col = int(location) - (3 * (row))

    if validateMove(row, col) is False:
        return False

    if player1Turn:
        board[row][col] = "O"
    else:
        board[row][col] = "X"
    
    return True

def validateMove(row, col):
    if (board[row][col] == "O" or board[row][col] == "X"):
        return False
    else:
        return True

def initializeGrid():
    '''Sets up the initial board'''
    rows, cols = (3,3)
    for i in range(rows):
        board.append([str(j + (i*3)) for j in range(cols)])
    return board

def printGrid(arr):
    '''Prints the current state of the board'''
    print("+ - + - + - +")
    for i in arr:
        print("|", end=" ")
        for j in i:
            print(str(j) + " |", end=" ")
        print()
        print("+ - + - + - +")

def checkWin():
    '''Checks if either player has won'''
    #Check horizontal
    for i in board:
        if i[0] == i[1] and i[0] == i[2]:
            foundWinner(i[0])
            return True

    #Check vertical
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            foundWinner(board[0][i])
            return True

    #Check diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            foundWinner(board[0][0])
            return True

    if board[0][2] == board[1][1] and board[0][0] == board[2][0]:
            foundWinner(board[0][2])
            return True

    return False

def foundWinner(token):
    '''Announces the winner based on if the token is a O or a X'''
    if (token == "O"):
        if (playingSinglePlayer is True):
            print("You won!")
        else:
            print("Player 1 wins!")
    else:
        if (playingSinglePlayer is True):
            print("You lost!")
        else:
            print("Player 2 wins!")

def computerTurn():
    '''Computer plays a random move'''
    location = randrange(9)
    while playMove(location) is False:
        location = randrange(9)
    printGrid(board)
    print()


if __name__ == "__main__":
    main()