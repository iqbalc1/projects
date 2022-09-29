#Tic Tac Game 

def sum(a, b, c ):
    return a + b + c
def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('Y' if zState[0] else 0)
    one = 'X' if xState[1] else ('Y' if zState[1] else 1)
    two = 'X' if xState[2] else ('Y' if zState[2] else 2)
    three = 'X' if xState[3] else ('Y' if zState[3] else 3)
    four = 'X' if xState[4] else ('Y' if zState[4] else 4)
    five = 'X' if xState[5] else ('Y' if zState[5] else 5)
    six = 'X' if xState[6] else ('Y' if zState[6] else 6)
    seven = 'X' if xState[7] else ('Y' if zState[7] else 7)
    eight = 'X' if xState[8] else ('Y' if zState[8] else 8)

    print (f" {zero} | {one} | {two}")
    print (f"---|---|---")
    print (f" {three} | {four} | {five}")
    print (f"---|---|---")
    print (f" {six} | {seven} | {eight}")

def checkwin(xState,zState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3) : 
            print("X has Win, Good Luck!")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3) : 
            print("Y has Win, Good Luck!")
            return 0
    return -1
    
if __name__ == "__main__" :
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn =1 #1 for x and 0 for 0 ###it means olny functions will be imported not code execution will be done ###we can also skip that
    print("Welcome to Tic Tac Toe . . . :)")
    print("Start Your Game Now !")
    while(True):
        printBoard(xState, zState)
        if (turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1 
        else: 
            print ("Y's chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1
        cwin= checkwin(xState,zState)
        if (cwin!=-1):
            print("Match Over!")
            break
        
        turn = 1 - turn 
        

            
    
    