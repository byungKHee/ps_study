import sys
input = sys.stdin.readline

C, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [-1] * 2000
dp[0] = 0

for i in range(0, 2000):
    if dp[i] == -1:
        continue
    for cost, member in arr:
        if i + member >= 2000: continue
        if dp[i + member] == -1:
            dp[i + member] = dp[i] + cost
        else:
            dp[i + member] = min(dp[i + member], dp[i] + cost)

print(min([n for n in dp[C:] if n != -1]))