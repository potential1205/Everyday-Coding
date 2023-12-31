import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lst1 = [i for i in range(1,n+1)]
    lst2 = [int(input()) for i in range(n)]
    
    board = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        board[lst1[i]-1][lst2[i]-1] = 1
    
    
    print("hello")
    for i in range(2):
        end = i
        t,f = 0,0
        answer = []
        while True:
            if board[t][f] == 1:
                t = f
                f = 0
                answer.append(t)
                if t == end:
                    print(answer)
                    break
            else:
                f+=1
                if f == n:
                    break

