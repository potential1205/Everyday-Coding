
from itertools import product
from collections import deque
import copy
from itertools import permutations;

def rotate_90(board):
    board = list(zip(*board))
    rotated_board = [list(row)[::-1] for row in board]
    return rotated_board

def rotate_num(board,num):
    for i in range(num):
        board = rotate_90(board)
    return board  


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(cube):
    if cube[0][0][0] == 0:
        return 9999
    
    queue = deque([[0,0,0,0]])
    visit = [[[False for k in range(5)] for j in range(5)] for i in range(5)]

    while queue:
        z,y,x,cnt = queue.popleft()

        if z==4 and y==4 and x==4:
            return cnt

        for i in range(6):
            kz,ky,kx = z+dz[i],y+dy[i],x+dx[i]

            if kz<0 or ky<0 or kx<0 or kz>=5 or ky>=5 or kx>=5 or visit[kz][ky][kx] == True or cube[kz][ky][kx] == 0:
                continue

            queue.append([kz,ky,kx,cnt+1])
            visit[kz][ky][kx] = True

    return 9999


if __name__ == "__main__":
    cube = []
    for i in range(5):
        face = []
        for j in range(5):
            line = list(map(int,input().split()))
            face.append(line)
        cube.append(face)
    
    combinations = list(product(range(4), repeat=5))
    min_move = 9999

    layer_combinations = list(permutations(range(5)))

    for i in range(len(combinations)):
        temp_cube = copy.deepcopy(cube)
        abc=[]

        for j in range(5):
            f = rotate_num(temp_cube[j],combinations[i][j])
            abc.append(f)
        
        temp_cube = []
        for l in range(len(layer_combinations)):
            for j in range(5):
                lr = layer_combinations[l][j]
                temp_cube.append(abc[lr])

        if temp_cube[0][0][0] !=0:
            val = bfs(temp_cube)
            min_move = min(min_move,val)

    if min_move == 9999:
        print(-1)
    else:
        print(min_move)

