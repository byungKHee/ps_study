import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

M, N = map(int, input().split())
arr = []
target = []
for i in range(N):
    arr.append(list(input().rstrip()))
    for j in range(M):
        if arr[i][j] == 'C':
            target.append([i,j])

visited = [[[float('inf')] * M for _ in range(N)] for _ in range(4)]
Q = deque()
x,y = target[0]
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    if arr[nx][ny] == '*':
        continue
    Q.append([nx,ny,0,i])
    visited[i][nx][ny] = 0

while Q:
    x,y,count,direction = Q.popleft()
    for i in range(4):
        ncount = count
        if direction != i:
            ncount += 1
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if arr[nx][ny] == '*':
            continue
        if ncount >= visited[i][nx][ny]:
            continue
        Q.append([nx,ny,ncount,i])
        visited[i][nx][ny] = ncount
a,b = target[1]
print(min([visited[i][a][b] for i in range(4)]))