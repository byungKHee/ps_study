from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    M = int(input())
    targets = list(map(int, input().split()))
    for target in targets:
        if bisect_right(arr, target) - bisect_left(arr, target):
            print(1)
        else:
            print(0)