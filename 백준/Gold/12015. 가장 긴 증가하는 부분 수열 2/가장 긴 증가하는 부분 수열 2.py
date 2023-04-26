import sys
input = sys.stdin.readline

def binarySearch(target):
    start = 0
    end = len(dp) - 1
    # (start, end] form
    while start+1 < end:
        mid = (start + end) // 2
        if dp[mid] < target:
            start = mid
        else:
            end = mid
    return end

N = int(input())
arr = list(map(int, input().split()))
dp = [0, arr[0]]

for n in arr[1:]:
    if dp[-1] < n:
        dp.append(n)
    else:
        idx = binarySearch(n)
        dp[idx] = n
print(len(dp)-1)