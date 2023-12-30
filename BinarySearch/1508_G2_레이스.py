



if __name__ == "__main__":
    n,m,k = map(int,input().split())
    lst = list(map(int,input().split()))

    start,end = 0,n
    result = []

    if m==2:
        for i in range(len(lst)):
            if i == 0 or i == len(lst)-1:
                print(1,end='')
            else:
                print(0,end='')
        exit()

    while start+1 < end:
        mid = (start+end)//2

        cnt=0
        val=0
        points=[]
        
        for i in range(len(lst)):
            if val <= lst[i]:
                cnt+=1
                val = lst[i]+mid
                if cnt <= m:
                    points.append(i)
            else:
                continue
        
        if cnt < m:
            end = mid
        elif cnt >= m:
            start = mid
            result = points[:]

    for i in range(len(lst)):
        if i in result:
            print(1,end='')
        else:
            print(0,end='')