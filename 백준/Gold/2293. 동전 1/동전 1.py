import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
dp = [0] * (K+1)
dp[0] = 1
for coin in coins:
    for total in range(K+1):
        if total - coin < 0:
            continue
        dp[total] += dp[total-coin]
print(dp[K])