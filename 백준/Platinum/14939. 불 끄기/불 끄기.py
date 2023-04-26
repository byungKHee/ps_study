import sys
import copy
input = sys.stdin.readline

IMPOSIBBLE = 1000
dx = [1,-1,0,0,0]
dy = [0,0,-1,1,0]

def press(arr, x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
            continue
        if arr[nx][ny]:
            arr[nx][ny] = False
        else:
            arr[nx][ny] = True

def check(case, arr):
    count = 0
    for i in range(10):
        if case & (1 << i):
            press(arr, 0, i)
            count += 1
    for i in range(9):
        for j in range(10):
            if arr[i][j]:
                press(arr, i+1, j)
                count += 1
    if any(arr[9]):
        return IMPOSIBBLE
    else:
        return count

Arr = [[False for _ in range(10)] for _ in range(10)]
for i in range(10):
    temp = input().rstrip()
    for j in range(10):
        if temp[j] == 'O':
            Arr[i][j] = True

answer = [IMPOSIBBLE] * 1024
for case in range(1024):
    answer[case] = check(case, copy.deepcopy(Arr))
print(min(answer))