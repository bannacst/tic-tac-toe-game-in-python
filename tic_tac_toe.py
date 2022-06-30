board=[' ' for x in range(10)]

def insertletter(letter,pos):
    board[pos]=letter 

def spaceisfree(pos):
    return board[pos]== ' '

def printboard(board):
    print('   |   |')
    print(' '+board[1] + ' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('----------------')
    print('   |   |')
    print(' '+board[4] + ' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('----------------')
    print('   |   |')
    print(' '+board[7] + ' | '+board[8]+' | '+board[9])
    print('   |   |')


def iswinner(bo,le):
    return (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3]==le) or (bo[1]==le and bo[4]==le and bo[7]==le) or        (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le)

def playermove():
    run = True
    while run:
        move=input("please enter a number to place an \'X\' (1-9): ")
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceisfree(move):
                    run=False
                    insertletter('x',move)
                else:
                    print("sorry occupied space")
            else:
                print("please enter within range")
        except:
            print("please type a number")

def compmove():
    possiblemoves=[x for x,letter in enumerate(board) if letter == ' ' and x!=0]
    move=0

    for let in ['o','x']:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if iswinner(boardcopy,let):
                move=i
                return move
    cornersopen=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move=selectrandom(cornersopen)
        return move
    if 5 in possiblemoves:
        move=5
        return move
    edgesopen=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesopen.append(i)
    if len(edgesopen)>0:
        move=selectrandom(edgesopen)
    return move

def selectrandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def isboardfull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
         

def main():
    print("welcome")
    printboard(board)
    while not(isboardfull(board)):
        if not(iswinner(board,'o')):
           playermove()
           printboard(board)
        else:
            print("sorry computer won this time")
            break 
        if not(iswinner(board,'x')):
           move=compmove()
           if move == 0:
                print("tie game")
           else:
                insertletter('o',move)
                print("computer place an \'o\' at position",move,":")
                printboard(board)
        else:
            print("you won this time")
            break
    

    if isboardfull(board):
        print("tie game")
         

flag=True
while flag:
    main()
    flag=input("do you want to play again say 0 or 1")
