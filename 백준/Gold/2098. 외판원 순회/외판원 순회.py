import sys
input = sys.stdin.readline

def func(curr, visited):
    if visited + 1 == (1 << N):
        if W[curr][0]:
            dp[curr][visited] = W[curr][0]
        else:
            dp[curr][visited] = float('inf')
        return dp[curr][visited]
    if dp[curr][visited] != -1:
        return dp[curr][visited]    
    dp[curr][visited] = float('inf')
    for next in range(1, N):
        if not W[curr][next]:
            continue
        if visited & (1 << next):
            continue
        dp[curr][visited] = min(dp[curr][visited], W[curr][next] + func(next, visited | (1 << next)))    
    return dp[curr][visited]

N = int(input())
W = []
dp = [[-1] * (1 << N) for _ in range(N)]
for _ in range(N):
    W.append(list(map(int, input().split())))
print(func(0,1))