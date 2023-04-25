import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0, arr[0]]
for i in range(1, N):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        start = 0
        end = len(dp)
        while start + 1 < end:
            mid = (start + end) // 2
            if dp[mid] == arr[i]:
                start = mid-1
                break
            if dp[mid] < arr[i]:
                start = mid
            else:
                end = mid
        dp[start+1] = arr[i]
print(len(dp)-1)