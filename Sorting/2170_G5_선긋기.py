import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lines = [list(map(int,input().split())) for i in range(n)]

    lines.sort()
    answer = [lines[0][0],lines[0][1]]

    for i in range(1,len(lines)):
        a,b = answer[0],answer[1]
        flag1 = False

        if b>=lines[i][0] and b<lines[i][1]:
            flag1 = True
        
        if lines[i][0] < a and lines[i][1] >=a:
            answer[0] = lines[i][0]

        if flag1 == True:
            answer[1] = lines[i][1]


    print(answer[1]-answer[0]+1)
