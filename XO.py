x = 'X'
o = 'O'
empty = '_'
playing = x
global board
board = [[empty, empty, empty], [empty, empty, empty], [empty, empty, empty]]


def checkWin(board: list):
    # check rows
    for i in board:
        if i.count(x) == 3:
            return x
        elif i.count(o) == 3:
            return o
    # check columns
    for i in range(3):
        count = []
        for j in range(3):
            count.append(board[j][i])
        if count.count(x) == 3:
            return x
        elif count.count(o) == 3:
            return o

    count1 = []
    count2 = []
    for i in range(3):
        count1.append(board[i][i])
        count2.append(board[i][2 - i])

    if count1.count(x) == 3 or count2.count(x) == 3:
        return x
    elif count1.count(o) == 3 or count2.count(o) == 3:
        return o

    return False


def checkValidMove(board: list, r: int, c: int) -> bool:
    # check if the move is valid
    if r in range(3) and c in range(3) and board[r][c] == empty:
        return True
    return False


def makeMove(r: int, c: int, play: str) -> bool:
    # make a move and check input
    global board
    if checkValidMove(board, r, c):
        board[r][c] = play
        return True
    return False


def checkIfTie(board: list) -> bool:
    # check if the board full
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != empty:
                count += 1
    return count == 9


def resetBoard() -> None:
    global board
    board = [[empty, empty, empty], [empty, empty, empty], [empty, empty, empty]]


def printBoard():
    global board
    for i in board:
        for j in i:
            print('{}'.format(j), end=' ')
        print(' ')


def playAgain() -> bool:
    i = input("To paly again enter 'y' : ")
    if i.lower() == 'y':
        return True
    return False


while True:
    try:
        r, c = input("Enter your move [Row Column]:").split()
    except:
        r, c = 5, 5

    if makeMove(int(r), int(c), playing):
        printBoard()
        if playing == x:
            playing = o
        else:
            playing = x

        if checkWin(board):
            print('{} Win!!'.format(checkWin(board)))
            if playAgain():
                resetBoard()
            else:
                break
        elif checkIfTie(board):
            print('Tie!!!!')
            if playAgain():
                resetBoard()
            else:
                break
    else:
        print('Bad move!!')
