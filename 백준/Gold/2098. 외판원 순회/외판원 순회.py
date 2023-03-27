import sys
input = sys.stdin.readline
IMPOSSIBLE = 10**9

def func(start, visited):
    if visited == (1 << N) - 1:
        if W[start][0]:
            dp[start][visited] = W[start][0]
        else:
            dp[start][visited] = IMPOSSIBLE
        return dp[start][visited]
        
    if dp[start][visited] != float('inf'):
        return dp[start][visited]

    for next in range(1, N):
        if not W[start][next]:
            continue
        if visited & (1 << next):
            continue
        next_cost = func(next, visited | (1 << next))
        if next_cost == IMPOSSIBLE:
            continue
        else:
            dp[start][visited] = min(dp[start][visited], next_cost + W[start][next])
    if dp[start][visited] == float('inf'):
        dp[start][visited] = IMPOSSIBLE
    return dp[start][visited]

N = int(input())
W = []
dp = [[float('inf')] * (1 << N) for _ in range(N)]
for i in range(N):
    W.append(list(map(int, input().split())))
print(func(0, 1))