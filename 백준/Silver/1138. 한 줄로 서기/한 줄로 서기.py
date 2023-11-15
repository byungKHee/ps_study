import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = [0] * N
number = list(range(N))

for i in range(N):
    answer[number.pop(arr[i])] = i+1
print(*answer)