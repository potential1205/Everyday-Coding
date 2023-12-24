from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def solution(sy,sx):

    queue = deque([[sy,sx]])

    

    
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
        
        for i in range(len(dirty)):
            print(dirty[i])
        
        

        

        
