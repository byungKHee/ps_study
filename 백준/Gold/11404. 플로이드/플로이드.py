import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
dp = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    dp[i][i] = 0
for _ in range(M):
    a,b,w = map(int, input().split())
    dp[a][b] = min(dp[a][b], w)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(dp[i][j], end=" ")
    print()