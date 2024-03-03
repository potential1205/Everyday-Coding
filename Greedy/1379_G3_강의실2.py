import heapq


if __name__ == "__main__":
    n = int(input())
    lectures = []
    for i in range(n):
        a,b,c = map(int,input().split())
        heapq.heappush(lectures,[b,c,a])

    end_time = [0]
    cnt = 1
    max_cnt = 0

    while lectures:
        a,b,c = heapq.heappop(lectures)

        if end_time[0] > a:
            if max_cnt - cnt > 0:
                cnt+=1
            else:
                cnt+=1
                max_cnt+=1
        else:
            while end_time and end_time[0] <= a:
                end_time.pop(0)
                cnt-=1
        
        print(cnt)
        cnt+=1
        end_time.append(b)
        end_time.sort()


    print(max_cnt)

