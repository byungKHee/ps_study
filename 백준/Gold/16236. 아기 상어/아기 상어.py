import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def search(x,y):
    visited = [[False] * N for i in range(N)]
    visited[x][y] = True
    Q = deque()
    Q.append([x,y,0])
    rnt = []
    while Q:
        cx, cy, dis = Q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny] > size:
                continue
            if 0 < arr[nx][ny] < size:
                rnt.append([dis+1, nx, ny])
            Q.append([nx, ny, dis+1])
            visited[nx][ny] = True
    if not rnt:
        return []
    rnt.sort()
    arr[rnt[0][1]][rnt[0][2]] = 0
    return rnt[0][1], rnt[0][2], rnt[0][0]

N = int(input())
arr = []
target = []
cx, cy = 0, 0
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 9:
            cx, cy = i, j
            arr[i][j] = 0
        elif arr[i][j] != 0:
            target.append([i,j])

size = 2
exp = 0
time = 0
while True:
    next = search(cx, cy)
    if not next:
        break
    cx, cy, dis = next
    time += dis
    exp += 1
    if exp >= size:
        exp = 0
        size += 1
print(time)