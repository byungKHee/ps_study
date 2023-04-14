import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))
arr = dict()
for n in card:
    if n in arr:
        arr[n] += 1
    else:
        arr[n] = 1
for n in target:
    if n in arr:   
        print(arr[n], end = ' ')
    else:
        print(0, end = ' ')