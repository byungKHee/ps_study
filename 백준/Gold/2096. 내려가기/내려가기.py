import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0,0,0]
min_dp = [0,0,0]
max_temp = [0,0,0]
min_temp = [0,0,0]

for i in range(N):
    arr = list(map(int, input().rstrip().split()))
    if i == 0:
        for j in range(3):
            max_temp[j] = arr[j]
            min_temp[j] = arr[j]
    else:
        max_temp[0] = arr[0] + max(max_dp[0], max_dp[1])
        min_temp[0] = arr[0] + min(min_dp[0], min_dp[1])
        max_temp[1] = arr[1] + max(max_dp[0], max_dp[1], max_dp[2])
        min_temp[1] = arr[1] + min(min_dp[0], min_dp[1], min_dp[2])
        max_temp[2] = arr[2] + max(max_dp[2], max_dp[1])
        min_temp[2] = arr[2] + min(min_dp[2], min_dp[1])
    for j in range(3):
        max_dp[j] = max_temp[j]
        min_dp[j] = min_temp[j]
print(f"{max(max_dp)} {min(min_dp)}")