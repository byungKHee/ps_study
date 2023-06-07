import sys
input = sys.stdin.readline
DIVIDE = 1_000_000_007

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
dp = [-1] * (N+1)
dp[0] = 1
dp[1] = 2
answer = 0
for i in range(N):
    answer += (arr[i] * (pow(2,i) - 1)) - (arr[i] * (pow(2,N-i-1) - 1))
    answer %= DIVIDE
print(answer)