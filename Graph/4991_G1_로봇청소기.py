from collections import deque
from itertools import permutations

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy,sx,ey,ex):
    queue = deque([[sy,sx,0]])
    visited = [[False for j in range(w)] for i in range(h)]
    cnt=0
    while queue:
        y,x,cnt = queue.popleft()

        for i in range(4):
            ky, kx = y+dy[i], x+dx[i]

            if ky<0 or kx<0 or ky>=h or kx>=w or visited[ky][kx] == True or board[ky][kx] == 'x':
                continue
            
            if ky == ey and kx == ex:
                return cnt+1

            queue.append([ky,kx,cnt+1])
            visited[ky][kx] = True

    return -1
    
if __name__ == "__main__":
    while True:
        w,h = map(int,input().split())
        if w == 0 and h == 0:
            break
         
        board,robot,dirty = [],[],[]
        for i in range(h):
            line = list(input())
            board.append(line)
            for j in range(w):
                if line[j] == '*':
                    dirty.append([i,j])
                elif line[j] == 'o':
                    robot.append([i,j])


        visit = []
        lst = [0] * len(dirty)
        for i in range(len(dirty)):
            lst[i] = bfs(robot[0][0],robot[0][1],dirty[i][0],dirty[i][1])

        a = [i for i in range(len(dirty))]

        candidate = list(permutations(a))

        dist = [[0 for i in range(len(dirty))] for j in range(len(dirty))]
        visit = []
        for i in range(len(dirty)):
            visit.append(i)
            for j in range(len(dirty)):
                if j not in visit:
                    sy,sx = dirty[i]
                    ey,ex = dirty[j]
                    dist[i][j] = bfs(sy,sx,ey,ex)

        print(candidate)
        print(lst,end='\n\n')
        for i in range(len(dist)):
            print(dist[i],end='\n')
        print("\n")

        
        for i in range(len(candidate)):
            print(candidate[i])
            temp = lst[candidate[i][0]]
            


        # answer = 9999
        # for i in range(len(lst)):
        #     temp = lst[i]
        #     start = i

        #     for j in range(len(candidate)):
        #         end = lst[j]
        #         temp += dist[start][end]


        

        

        
