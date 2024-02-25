import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lines = [list(map(int,input().split())) for i in range(n)]

    lines.sort(key = lambda x : (x[0],-x[1]))
    answer = [lines[0][0],lines[0][1]]
    result = []
    
    for i in range(1,len(lines)):
        start,end = lines[i]

        if start == answer[0]:
            continue

        if start <= answer[1]:
            if end > answer[1]:
                answer[1] = end
        else:
            result.append(answer[1]-answer[0])
            answer[0], answer[1] = start,end
    
    result.append(answer[1]-answer[0])
    

    print(result)
    print(sum(result))
