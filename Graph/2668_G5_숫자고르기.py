import sys
input = sys.stdin.readline

from itertools import permutations

def solution(level,lst):
    
    for i in range(n):
        lst.append(lst1[i])
        solution()
        lst.pop(-1)



if __name__ == "__main__":
    n = int(input())
    lst1 = [i for i in range(1,n+1)]
    lst2 = [int(input()) for i in range(n)]
    
    board = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        board[lst1[i]-1][lst2[i]-1] = 1
    
    answer = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and board[j][i] == 1:
                answer.append(i+1)
            else:
                continue
    
    answer = list(set(answer))
    answer.sort()
    print(len(answer))
    for val in set(answer):
        print(val)
             