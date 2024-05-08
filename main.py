import copy
brd = [[[None], [None], [None]],
         [[None], [None], [None]],
         [[None], [None], [None]]]

def checkrow(board):
    lst = []
    for i in range(0,3):
        for j in range(0,3):
            lst += board[i][j]

    for a in range(0,7,3):
        if len(set(lst[a:a+3])) == 1 and set(lst[a:a+3]) != {None}:
            return lst[a:a+3][0]
        else:
            pass
    return 0
          
def checkcolumn(board):
    lst = []
    for i in range(0,3):
        for j in range(0,3):
            lst += board[j][i]
    
    for a in range(0,7,3):
        if len(set(lst[a:a+3])) == 1 and set(lst[a:a+3]) != {None}:
            return lst[a:a+3][0]
        else:
            pass
    return 0


def checkdiag(board):
    lst1 = []
    for i in range(3):
        lst1 += board[i][i]

    if len(set(lst1)) == 1 and set(lst1) != {None}:
        return lst1[0]
    else:
        pass

    lst2 = []
    for i in range(3):
        lst2 += board[i][2-i]
    
    if len(set(lst2)) == 1 and set(lst2) != {None}:
        return lst2[0]
    else:
        pass

    return 0


def checkwin(board):
    lst = [checkrow(board), checkcolumn(board), checkdiag(board)]
    new = sorted(lst, reverse= True)
    return(new[0])


def checkfull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j][0] == None:
                return 0
    return 3
#3 is full

#human = 1
#bot = 2
def playermove(coor:tuple):
    if brd[coor[0]][coor[1]][0] == None:
        brd[coor[0]][coor[1]][0] = 1
    else:
        return 'Occupied'
    
def botmove(coor):
    brd[coor[0]][coor[1]][0] = 2

def getempty(board):
    lst = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == [None]:
                lst.append((i,j))
    return lst

    
def minimax(board, alpha, beta, bot:bool):
    nummt = len(getempty(board)) + 1
    #bot win
    if checkwin(board) == 2:
        return 1*nummt, None
    #human win
    if checkwin(board) == 1:
        return -1*nummt, None
    #full
    elif checkfull(board) == 3:
        return 0, None
    
    if bot:#alpha
        maxvalue = -100
        bestmove = None
        mtlist = getempty(board)
        for space in mtlist:
            col = space[0]
            row = space[1]
            vboard = copy.deepcopy(board)
            vboard[col][row][0] = 2
            mini = minimax(vboard, alpha, beta, False)
            value = mini[0]
            if value > maxvalue:
                maxvalue = value
                bestmove = space
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return maxvalue, bestmove
                
    elif  not bot:#beta
        minvalue = 100
        bestmove = None
        mtlist = getempty(board)
        for space in mtlist:
            col = space[0]
            row = space[1]
            vboard = copy.deepcopy(board)
            vboard[col][row][0] = 1
            maxe = minimax(vboard, alpha, beta, True)
            value = maxe[0]
            if value < minvalue:
                minvalue = value
                bestmove = space
            beta = min(beta, value)
            if beta <= alpha:
                break
        return minvalue, bestmove

def printboard():
    board = copy.deepcopy(brd)
    for i in range(3):
        for j in range(3):
            if board[i][j][0] == None:
                board[i][j][0] = ' '
            elif board[i][j][0] == 1:
                board[i][j][0] = 'X'
            elif board[i][j][0] ==2:
                board[i][j][0] = 'O'
    print('  1   2   3')
    print("A %s | %s | %s  "%(board[0][0][0],board[0][1][0],board[0][2][0]))    
    print(" ___|___|___")    
    print("B %s | %s | %s  "%(board[1][0][0],board[1][1][0],board[1][2][0]))    
    print(" ___|___|___")    
    print("C %s | %s | %s  "%(board[2][0][0],board[2][1][0],board[2][2][0]))      
    print("    |   |  ") 

def checkwinfull():
    if checkwin(brd) == 2:
        print('U lose, bot win')
        return False
    elif checkwin(brd) == 1:
        print('U win')
        return False
    elif checkfull(brd) == 3:
        print('Tie')
        return False
    else:
        return True

def checkoccu():
    coor = input('Enter where u want to play:')
    vert = ['A', 'B', 'C']
    ncoor = (ord(coor[0])-65, int(coor[1])-1)
    if coor[0] not in vert or int(coor[1]) not in range(1,4):
        return 1
    elif brd[ncoor[0]][ncoor[1]][0] != None:
        return 1
    else:
        return ncoor

def convert(coor):
    col = chr(coor[0]+65)
    row = coor[1]+1
    return f"{col}{row}"

def main():
    x = input('choose play 1st or 2nd:')
    printboard()
    while True:
        print('pls enter vertical first')
        if x != '1':
            pass
        else:
            good = False
            while not good:
                coor = checkoccu()
                if  coor == 1:
                    pass
                else:
                    playermove(coor)
                    printboard()
                    good = True
            x = '1'

        if checkwinfull() == False:
            break

        bot = minimax(brd, -float('inf'), float('inf'), True)
        print(bot)
        botmove(bot[1])
        print(f"AI chose {convert(bot[1])}")
        printboard()
        if checkwinfull() == False:
            break

main()
        
        

