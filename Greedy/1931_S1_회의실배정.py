
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        line = list(map(int,input().split()))
        lst.append([line[1],line[0]])
    
    lst.sort()
    cnt = 0
    std = lst[0][0]
    cnt+=1

    for i in range(1,n):
        end,start = lst[i]
        if std <= start:
            cnt+=1
            std = end
            
        else:
            continue


    print(cnt)
