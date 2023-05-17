import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def reset():
    for i in range(N):
        for j in range(M):
            visited[i][j] = False

def bfs(x,y):
    visited[x][y] = True
    Q = deque()
    Q.append([x,y,0])
    rnt = 0
    while Q:
        x,y,dis = Q.popleft()
        rnt = max(rnt, dis)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and arr[nx][ny] == 'L':
                Q.append([nx,ny,dis+1])
                visited[nx][ny] = True
    return rnt

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))

answer = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            reset()
            answer = max(answer, bfs(i,j))
print(answer)