import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
left = arr[:N//2]
leftSum = []
right = arr[N//2:]
rightSum = []
answer = 0
for i in range(1, len(left)+1):
    for comb in combinations(left, i):
        temp = sum(comb)
        if temp == S:
            answer += 1
        leftSum.append(temp)
for i in range(1, len(right)+1):
    for comb in combinations(right, i):
        temp = sum(comb)
        if temp == S:
            answer += 1
        rightSum.append(temp)

leftSum.sort()
rightSum.sort(reverse=True)
leftSum.append(10**8)
rightSum.append(10**8)
l = 0; r = 0
while True:
    curr = leftSum[l] + rightSum[r]
    if curr == S:
        currL = l; currR = r
        while leftSum[currL] == leftSum[l]:
            l += 1
        while rightSum[currR] == rightSum[r]:
            r += 1
        answer += (l-currL) * (r-currR)            
    elif curr > S:
        r += 1
    elif curr < S:
        l += 1
    if r == len(rightSum) or l == len(leftSum):
        break
print(answer)