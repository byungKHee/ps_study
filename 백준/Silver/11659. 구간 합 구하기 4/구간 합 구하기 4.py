import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
for i in range(1, N):
    arr[i] += arr[i-1]
arr.append(0)
for _ in range(M):
    s, e = map(int, input().split())
    print(arr[e-1] - arr[s-2])