import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
memory.insert(0,0)
cost = list(map(int, input().split()))
cost.insert(0,0)
dp = [[0 for _ in range(sum(cost)+1)] for _ in range(N+1)]
answer = sum(cost) + 1
for i in range(1, N+1):
    for j in range(1, sum(cost)+1):
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + memory[i])
        if dp[i][j] >= M:
            answer = min(answer, j)
print(answer)