import sys
from itertools import product
from copy import deepcopy
input = sys.stdin.readline

rotate = [[0,], [0,1,2,3], [0,1], [0,1,2,3], [0,1,2,3], [0]]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def fill(x, y, d, arr):
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        if arr[nx][ny] == 6:
            break
        if 1 <= arr[nx][ny] <= 5:
            x,y = nx,ny
            continue
        arr[nx][ny] = 7
        x, y = nx, ny

def func(case, arr):
    for i,(x,y) in enumerate(cctv):
        if arr[x][y] == 1:
            fill(x,y,case[i],arr)
        elif arr[x][y] == 2:
            fill(x, y, case[i], arr)
            fill(x, y, case[i]+2, arr)
        elif arr[x][y] == 3:
            fill(x, y, case[i], arr)
            fill(x, y, (case[i]+1) % 4, arr)
        elif arr[x][y] == 4:
            fill(x, y, case[i], arr)
            fill(x, y, (case[i]+1) % 4, arr)
            fill(x, y, (case[i]+2) % 4, arr)
        else:
            fill(x, y, 0, arr)
            fill(x, y, 1, arr)
            fill(x, y, 2, arr)
            fill(x, y, 3, arr)
    count = 0
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                count += 1
    return count

N, M = map(int, input().split())
arr = []
cctv = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctv.append([i,j])
direction = []
for x,y in cctv:
    direction.append(rotate[arr[x][y]])

answer = N*M
for case in product(*direction):
    answer = min(answer, func(case, deepcopy(arr)))
print(answer)