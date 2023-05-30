import sys
input = sys.stdin.readline

def func(day):
    rnt = 0
    for i in range(day, N):
        if i + arr[i][0] <= N:
            rnt = max(rnt, arr[i][1] + func(i+arr[i][0]))
    return rnt
    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(func(0))