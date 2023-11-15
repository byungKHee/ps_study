import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
number = [0] * (max(arr) + 1)
answer = 1
l = 0
r = 0

target = 0
while r < N:
    if not target:
        number[arr[r]] += 1
        if number[arr[r]] > K:
            target = arr[r]
        else:
            answer = max(answer, r-l+1)
        r += 1
    else:
        number[arr[l]] -= 1
        if target == arr[l]:
            target = 0
        l += 1
print(answer)