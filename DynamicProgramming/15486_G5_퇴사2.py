
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lst = [0] + [list(map(int,input().split())) for i in range(n)]
    dp = [0] * (n+1)

    for i in range(1,n+1):
        dp[i] = max(dp[i], dp[i-1])
        day,profit = lst[i]
        if i+day-1 <= n:
            dp[i+day-1] = max(dp[i+day-1], dp[i-1]+profit)
    
    print(dp[-1])
