import sys
from itertools import combinations
input = sys.stdin.readline

def add(a,b):
    return [a[0] + b[0], a[1] + b[1]]

def minus(a,b):
    return [a[0] - b[0], a[1] - b[1]]

for testCase in range(int(input())):
    N = int(input())
    point = []
    for _ in range(N):
        point.append(list(map(int, input().split())))
    answer = float('inf')
    for comb in combinations([i for i in range(N)], N//2):
        temp = [0,0]
        for idx in range(N):
            if idx in comb:
                temp = minus(temp, point[idx])
            else:
                temp = add(temp, point[idx])
        answer = min(answer, (temp[0]**2 + temp[1]**2)**0.5)
    print(answer)