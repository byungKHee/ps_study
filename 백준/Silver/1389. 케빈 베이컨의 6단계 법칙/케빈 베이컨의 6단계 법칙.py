import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[float('inf')] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1
for i in range(1, N+1):
    dp[i][i] = 0
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
count = [0] * (N+1)
MIN = float('inf')
for i in range(1, N+1):
    for j in range(1, N+1):
        count[i] += dp[i][j]
    MIN = min(MIN, count[i])
for i in range(1, N+1):
    if count[i] == MIN:
        print(i)
        break