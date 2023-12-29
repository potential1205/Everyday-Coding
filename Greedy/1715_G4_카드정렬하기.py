import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    if n==1:
        print(0)
    else:
        lst = []
        for i in range(n):
            heapq.heappush(lst,int(input()))
        answer,cnt = 0, 0
        while True:
            if len(lst) > 1:
                val1 = heapq.heappop(lst)
                val2 = heapq.heappop(lst)
                cnt = val1+val2
                answer += (cnt)
                heapq.heappush(lst,cnt)
                cnt = 0
            else:
                break

        print(answer)