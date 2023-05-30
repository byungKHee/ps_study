import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)
for day in range(N):
    for i in range(day, N):
        if i + arr[i][0] <= N:
            dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[day] + arr[i][1])
print(max(dp))