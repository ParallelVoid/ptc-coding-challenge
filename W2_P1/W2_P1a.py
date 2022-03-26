import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
if n >= 1 and n <=20 and n >= 1 and n <=20:
    board = []
    for y in range(0, m):
        row = []
        for x in range(0, n):
            row.append(1)
        board.append(row)


    for y in range (1, m):
        for x in range(1, n):
            val = board[y][x-1] + board[y-1][x]
            ty = y-1
            board[y][x] = val

    print(board[m-1][n-1])
else:
    print("The maze is too large")