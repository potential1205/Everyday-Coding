
from collections import deque

if __name__ == "__main__":
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append((a,b))
        y.append((b,a))

    x.sort()
    y.sort()

    max_h = y[-1][0]
    stack = deque([[x[0][0],x[0][1]]])

    for i in range(1,n):
        kx,ky = x[i]
        if ky == max_h:
            stack.append([kx,ky])

            idx = i+1
            break

        if stack[-1][1] < ky:
            stack.append([kx,ky])
        else:
            continue
    
    stack2 = deque([[x[idx][0],x[idx][1]]])

    for i in range(idx+1,n):
        kx,ky = x[i]

        if stack2[-1][1] < ky:
            while stack2:
                stack2.popleft()
            stack2.append([kx,ky])
        else:
            stack2.append([kx,ky])

    answer = 0

    for i in range(len(stack)-1):
        gap = stack[i+1][0] - stack[i][0]
        answer = answer + gap*stack[i][1]
    
    answer += max_h

    a,b = stack2.popleft()
    answer += (a-stack[i+1][0])*b

    for i in range(len(stack2)-1):
        gap = stack2[i+1][0] - stack2[i][0]
        answer = answer + gap*stack2[i+1][1]
    

    print(answer)

