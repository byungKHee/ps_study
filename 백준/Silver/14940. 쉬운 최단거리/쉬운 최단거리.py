import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int, input().split())
arr = []
dis = [[0] * M for _ in range(N)]
Q = deque()

for i in range(N):
    arr.append(list(map(int, input().rstrip().split())))
    for j in range(M):
        if arr[i][j] == 2:
            Q.append([i,j])

while Q:
    cx, cy = Q.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if arr[nx][ny] == 0 or arr[nx][ny] == 2:
            continue
        if dis[nx][ny] != 0:
            continue
        dis[nx][ny] = dis[cx][cy] + 1
        Q.append([nx,ny])

for i in range(N):
    for j in range(M):
        if dis[i][j] == 0 and arr[i][j] == 1:
            dis[i][j] = -1
            
for i in dis:
    print(*i)