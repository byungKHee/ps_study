import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def get_size(x,y):
    rnt = 0
    visited[x][y] = True
    Q = deque()
    Q.append((x,y))
    while Q:
        cx, cy = Q.popleft()
        rnt += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not arr[nx][ny] or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            Q.append((nx,ny))
    return rnt

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

count = 0
answer = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            answer = max(answer, get_size(i,j))
            count += 1
print(count)
print(answer)