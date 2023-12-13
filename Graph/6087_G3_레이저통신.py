from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    start, end = point[0], point[1]
    queue = deque([[start[0],start[1],0]])
    visit = [[False for j in range(w)] for i in range(h)]


    while queue:
        y,x,cnt = queue.popleft()

        if y==end[0] and x==end[1]:
            return cnt
        
        for i in range(4):
            ky,kx = y+dy[i], x+dx[i]
            if 0<=kx and kx<w and 0<= ky and ky<h and visit[ky][kx]==False and board[ky][kx] != '*':
                visit[ky][kx]=True
                queue.append([ky,kx,cnt+1])
    
    return cnt





w,h = map(int,input().split())
board, point = [], []

for i in range(h):
    line = input()
    for j in range(w):
        if line[j]=='C':
            point.append([i,j])
    board.append(line)

print(bfs())