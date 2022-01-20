from audioop import mul
from ipaddress import collapse_addresses
from nis import cat


def main():
    print("Welcome to Tic-Tac-Toe")

    mode = input("Please choose a game mode:")
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

    print("We good with " + str(modeInt))
    if (modeInt == 0):
        singlePlayerMode()
    elif (modeInt == 1):
        multiPlayerMode()

def singlePlayerMode():
    arr = initializeGrid()
    printGrid(arr)

def multiPlayerMode():
    print("Welcome to multiplayer")

def initializeGrid():
    arr = []
    rows, cols = (3,3)
    for i in range(rows):
        arr.append([(j + (i*3)) for j in range(cols)])
    return arr

def printGrid(arr):
    for i in arr:
        print("|", end=" ")
        for j in i:
            print(str(j) + " |", end=" ")
        print()

if __name__ == "__main__":
    main()