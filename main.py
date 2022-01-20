from audioop import mul
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
    print("Welcome to single player")

def multiPlayerMode():
    print("Welcome to multiplayer")

if __name__ == "__main__":
    main()