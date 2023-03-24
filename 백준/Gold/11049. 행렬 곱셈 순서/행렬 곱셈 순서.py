import sys
input = sys.stdin.readline

def mul(start, mid, end):
    return arr[start][0] * arr[mid][0] * arr[end-1][1]

N = int(input())
arr = []
dp = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N):
    arr.append(list(map(int, input().split())))
for dis in range(2, N+1):
    for start in range(N):
        end = start + dis
        if end > N:
            continue
        value = 2**31-1
        for mid in range(start+1, end):
            value = min(value, dp[start][mid] + dp[mid][end] + mul(start, mid, end))
        dp[start][end] = value
print(dp[0][N])