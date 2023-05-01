import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = arr1[::-1]
dp1 = [1] * N
dp2 = [1] * N
for i in range(1,N):
    for j in range(i):
        if arr1[j] < arr1[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if arr2[j] < arr2[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()
answer = [0] * N
for i in range(N):
    answer[i] = dp1[i] + dp2[i]
print(max(answer)-1)