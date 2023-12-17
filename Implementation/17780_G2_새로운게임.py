from collections import deque

def check():
    for i in range(n):
        for j in range(n):
            if len(board_queue[i][j])==4:
                return True
    return False

def rotate(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

if __name__ == "__main__":
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    n,k = map(int,input().split())
    board = []
    for _ in range(n):
        line = list(map(int,input().split()))
        board.append(line)

    board_queue = []
    for i in range(n):
        board_queue.append([])
        for j in range(n):
            board_queue[i].append(deque())

    players = []
    for i in range(k):
        y,x,d = map(int,input().split())
        players.append([y-1,x-1,d-1])
        board_queue[y-1][x-1].append(i)

    for turn in range(1000):
        for i in range(k):
            y,x,d = players[i]
            if board_queue[y][x][0] != i:
                continue

            ky, kx = y+dy[d], x+dx[d]

            if ky<0 or ky>=n or kx<0 or kx>=n or board[ky][kx] == 2:
                d = rotate(d)
                players[i][2] = d
                ky,kx = y+dy[d], x+dx[d]

                if 0<=ky<n and 0<=kx<n and board[ky][kx] != 2:
                    if board[ky][kx] == 0:
                        while board_queue[y][x]:
                            val = board_queue[y][x].popleft()
                            board_queue[ky][kx].append(val)
                            players[val][0], players[val][1] = ky,kx

                    elif board[ky][kx] == 1:
                        while board_queue[y][x]:
                            val = board_queue[y][x].pop()
                            board_queue[ky][kx].append(val)
                            players[val][0], players[val][1] = ky,kx      
                                          

            elif board[ky][kx] == 0:
                while board_queue[y][x]:
                    val = board_queue[y][x].popleft()
                    board_queue[ky][kx].append(val)
                    players[val][0], players[val][1] = ky,kx

            elif board[ky][kx] == 1:
                while board_queue[y][x]:
                    val = board_queue[y][x].pop()
                    board_queue[ky][kx].append(val)
                    players[val][0], players[val][1] = ky,kx
                

            if check():
                print(turn+1)
                exit()

    print(-1)

        