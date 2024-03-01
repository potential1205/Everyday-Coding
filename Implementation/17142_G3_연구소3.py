from collections import deque
from itertools import combinations

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(board,candidate):
    #print(candidate)
    visit = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = '-'
                visit[i][j] = -1
            elif board[i][j] == 2:
                board[i][j] = '*'

    queue = deque([])
    for i in range(m):
        y,x = candidate[i]
        queue.append([y,x])
        board[y][x] = 'O'
        visit[y][x] = 0
    

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ky,kx = y+dy[i],x+dx[i]

            if ky<0 or kx<0 or ky>=n or kx>=n or visit[ky][kx]!=0 or board[ky][kx] == '-' or board[ky][kx]=='O':
                continue
            
            if board[ky][kx] == '*':
                board[ky][kx] = 'O'
                visit[ky][kx] = visit[y][x]
                queue.append([ky,kx])
            else:
                queue.append([ky,kx])
                visit[ky][kx] = visit[y][x] + 1
    
    # for i in range(n):
    #     print(*board[i])
    # print()

    # for i in range(n):
    #     print(*visit[i])
    # print()

    cnt=0
    a = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and board[i][j] == 0:
                cnt+=1
            a = max(a,visit[i][j])
    
    print(cnt,a)
    if cnt==0:
       return a
    else:
        return -1 

if __name__ == "__main__":
    n,m = map(int,input().split())
    board = []
    virus = []
    for i in range(n):
        line = list(map(int,input().split()))

        for j in range(len(line)):
            if line[j] == 2:
                virus.append([i,j])
        board.append(line)

    candidate = list(combinations(virus,m))

    answer = 99999
    flag = False
    for i in range(len(candidate)):
        val = bfs(board,candidate[i])
        if val != -1:
            answer = min(answer,val)
            flag= True

    if flag:
        print(answer)
    else:
        print(-1)

    

