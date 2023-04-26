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
dp = [float('-inf'), arr[0]]
record = [(0, float('-inf')), (1, arr[0])]

for n in arr[1:]:
    if dp[-1] < n:
        dp.append(n)
        record.append((len(dp)-1, n))
    else:
        idx = binarySearch(n)
        dp[idx] = n
        record.append((idx, n))

answer = []
count = len(dp)-1
for idx, num in record[::-1]:
    if idx == count:
        answer.append(num)
        count -= 1
    if count == 0:
        break
print(len(dp)-1)
print(*answer[::-1])