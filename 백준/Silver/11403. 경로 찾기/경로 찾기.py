import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            dp[i][j] = float("inf")

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(N):
    for j in range(N):
        if dp[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()