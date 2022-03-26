import sys

def doWin(board):
    coordX = -1
    coordY = -1


    if board[0][0] == board[1][1] and board[0][0] == 'x':
        if board[2][2] == ".":
            coordY = 2
            coordX = 2
            return (coordX, coordY)

    if board[0][0] == board[2][2] and board[0][0] == 'x':
        if board[1][1] == ".":
            coordY = 1
            coordX = 1
            return (coordX, coordY)

    if board[1][1] == board[2][2] and board[1][1] == 'x':
        if board[0][0] == ".":
            coordY = 0
            coordX = 0
            return (coordX, coordY)
    
    if board[0][2] == board[1][1] and board[0][2] == 'x':
        if board[2][0] == ".":
            coordY = 2
            coordX = 0
            return (coordX, coordY)
    
    if board[0][2] == board[2][0] and board[0][2] == 'x':
        if board[1][1] == ".":
            coordY = 1
            coordX = 1
            return (coordX, coordY)
    
    if board[1][1] == board[2][0] and board[2][0] == 'x':
        if board[0][2] == ".":
            coordY = 0
            coordX = 2
            return (coordX, coordY)

    for row in range (0,3):
        # print(board[row])
        numO = 0
        for col in range (0, 3):
            if board[row][col] == 'x':
                numO+=1
        if numO == 2:
            coordY = row
            for x in range(0,3):
                if board[row][x] != 'x' and board[row][x] == '.':
                    coordX = x
                    break

            if coordX != -1:
                break
        
        if coordX != -1 and coordY != -1:
            
            return (coordX, coordY)


    # print("vertical step")
    for col in range (0,3):
        # print(board[row])
        numO = 0
        for row in range (0, 3):
            if board[row][col] == 'x':
                numO+=1
            if numO == 2:
                coordX = row
            # print(col)
                for y in range(0,3):
                    if board[y][row] != 'o' and board[y][row] == '.':
                        # print("Found Y")
                        coordY = y
                        break

            if coordX != -1:
                # print("Found x")
                return (coordX, coordY)
        
        if coordX != -1 and coordY != -1:
            return (coordX, coordY)


def doBlock(board):
    coordX = -1
    coordY = -1

    if board[0][0] == board[1][1] and board[0][0] == 'o':
        if board[2][2] == ".":
            coordY = 2
            coordX = 2
            return (coordX, coordY)

    if board[0][0] == board[2][2] and board[0][0] == 'o':
        if board[1][1] == ".":
            coordY = 1
            coordX = 1
            return (coordX, coordY)

    if board[1][1] == board[2][2] and board[1][1] == 'o':
        if board[0][0] == ".":
            coordY = 0
            coordX = 0
            return (coordX, coordY)
    
    if board[0][2] == board[1][1] and board[0][2] == 'o':
        if board[2][0] == ".":
            coordY = 2
            coordX = 0
            return (coordX, coordY)
    
    if board[0][2] == board[2][0] and board[0][2] == 'o':
        if board[1][1] == ".":
            coordY = 1
            coordX = 1
            return (coordX, coordY)
    
    if board[1][1] == board[2][0] and board[2][0] == 'o':
        if board[0][2] == ".":
            coordY = 0
            coordX = 2
            return (coordX, coordY)

    for row in range (0,3):
        # print(board[row])
        numO = 0
        for col in range (0, 3):
            if board[row][col] == 'o':
                numO+=1
        if numO == 2:
            coordY = row
            for x in range(0,3):
                if board[row][x] != 'o' and board[row][x] == '.':
                    coordX = x
                    break

            if coordX != -1:
                break
        
        if coordX != -1 and coordY != -1:
            return (coordX, coordY)


    # print("vertical step")
    for col in range (0,3):
        # print(board[row])
        numO = 0
        for row in range (0, 3):
            if board[row][col] == 'o':
                numO+=1
        if numO == 2:
            coordX = row
            # print(col)
            for y in range(0,3):
                if board[y][row] != 'o' and board[y][row] == '.':
                    # print("Found Y")
                    coordY = y
                    
                    break

            if coordX != -1:
                # print("Found x")
                return (coordX, coordY)
        
        if coordX != -1 and coordY != -1:
            return (coordX, coordY)

board = []
with open(sys.argv[1]) as file:
    result = [list(line.rstrip()) for (line) in file]

if len(result) != 3:
    exit()
else:
    command = ''.join(result[2])
    board = result[0: ]



xy = (-1,-1)
xy = doWin(board)
if xy[0] != -1 and xy[1] != -1:

    print("{} {}".format(int(xy[0]) + 1, int(xy[1]) + 1))
else:
    xy = doBlock(board)
    print("{} {}".format(int(xy[0]) + 1, int(xy[1]) + 1))
