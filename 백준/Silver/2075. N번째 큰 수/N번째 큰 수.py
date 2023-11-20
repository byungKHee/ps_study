import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
arr = []
for n in list(map(int, input().split())):
    heappush(arr, n)
for _ in range(N-1):
    for n in list(map(int, input().split())):
        heappush(arr,n)
        heappop(arr)
print(arr[0])