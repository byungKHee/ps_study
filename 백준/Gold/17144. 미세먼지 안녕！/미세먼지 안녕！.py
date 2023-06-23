import sys
from copy import deepcopy
input = sys.stdin.readline

Direction = [[1,0], [-1,0], [0,1], [0,-1]]
OutOfRange = lambda x, y : x < 0 or x >= N or y < 0 or y >= M

def spread():
    temp = deepcopy(arr)
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 0:
                continue
            if arr[x][y] == -1:
                temp[x][y] = -1
                continue
            count = 0
            for dx, dy in Direction:
                nx = x + dx
                ny = y + dy
                if OutOfRange(nx,ny) or arr[nx][ny] == -1:
                    continue
                count += 1
                temp[nx][ny] += arr[x][y] // 5
            temp[x][y] -= (arr[x][y] // 5) * count
    return temp

def purify():
    # up part
    arr[start[0]][0] = 0
    for x in range(start[0], 0, -1):
        arr[x][0] = arr[x-1][0]
    for y in range(0, M-1):
        arr[0][y] = arr[0][y+1]
    for x in range(0, start[0]):
        arr[x][M-1] = arr[x+1][M-1]
    for y in range(M-1, 1, -1):
        arr[start[0]][y] = arr[start[0]][y-1]
    arr[start[0]][1] = 0
    arr[start[0]][0] = -1
    # down part
    arr[start[1]][0] = 0
    for x in range(start[1], N-1):
        arr[x][0] = arr[x+1][0]
    for y in range(0, M-1):
        arr[N-1][y] = arr[N-1][y+1]
    for x in range(N-1, start[1], -1):
        arr[x][M-1] = arr[x-1][M-1]
    for y in range(M-1, 1, -1):
        arr[start[1]][y] = arr[start[1]][y-1]
    arr[start[1]][1] = 0
    arr[start[1]][0] = -1

N, M, T = map(int, input().split())
arr = []
start = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    if arr[i][0] == -1:
        start.append(i)

for t in range(T):
    arr = spread()
    purify()

answer = 2
for i in range(N):
    for j in range(M):
        answer += arr[i][j]
print(answer)