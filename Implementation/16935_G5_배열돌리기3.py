
def f1(board):
    global n,m
    for i in range(m):
        for j in range(n//2):
            board[j][i], board[n-j-1][i] = board[n-j-1][i], board[j][i]
    return board

def f2(board):
    global n,m
    for i in range(n):
        for j in range(m//2):
            board[i][j], board[i][m-j-1] = board[i][m-j-1], board[i][j]
    return board

def f3(board):
    global n,m
    board = list(map(list, zip(*board[::-1])))
    n,m = m,n
    return board

def f4(board):
    global n,m
    board = list(map(list, zip(*board)))[::-1]
    n,m = m,n
    return board

def f5(board):
    global n,m
    for i in range(n//2):
        for j in range(m//2):
            temp = board[i][j]
            board[i][j] = board[i+n//2][j]
            board[i+n//2][j] = board[i+n//2][j+m//2]
            board[i+n//2][j+m//2] = board[i][j+m//2]
            board[i][j+m//2] = temp
    return board

def f6(board):
    global n,m
    for i in range(n//2):
        for j in range(m//2):
            temp = board[i][j]
            board[i][j] = board[i][j+m//2]
            board[i][j+m//2] = board[i+n//2][j+m//2]
            board[i+n//2][j+m//2] = board[i+n//2][j]
            board[i+n//2][j] = temp

    return board

if __name__ == "__main__":
    n,m,r = map(int,input().split())
    board = []
    for i in range(n):
        board.append(list(map(int,input().split())))
    
    ops = list(map(int,input().split()))
    
    for op in ops:
        if op == 1:
            board = f1(board)
        elif op == 2:
            board = f2(board)
        elif op == 3:
            board = f3(board)
        elif op == 4:
            board = f4(board)
        elif op == 5:
            board = f5(board)
        elif op == 6:
            board = f6(board)

    for i in range(len(board)):
        print(*board[i])