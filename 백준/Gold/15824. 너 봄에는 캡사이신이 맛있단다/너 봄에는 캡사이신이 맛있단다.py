import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
DIVIDE = 1_000_000_007

def pow(n):
    if dp[n] != -1:
        return dp[n]
    if n % 2 == 0:
        half = pow(n//2)
        dp[n] = half * half % DIVIDE
        return dp[n]
    else:
        half = pow(n//2)
        dp[n] = half * half * 2 % DIVIDE
        return dp[n]

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
dp = [-1] * (N+1)
dp[0] = 1
dp[1] = 2
plus = 0
minus = 0
for i in range(N):
    if i == 0:
        minus += arr[i] * (pow(N-i-1) - 1) % DIVIDE
    elif i == N-1:
        plus += arr[i] * (pow(i) - 1) % DIVIDE
    else:
        plus += arr[i] * (pow(i) - 1) % DIVIDE
        minus += arr[i] * (pow(N-i-1) - 1) % DIVIDE
print((plus - minus) % DIVIDE)