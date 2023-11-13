import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    next = []
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((0,0))
    while Q:
        cx, cy = Q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == -1:
                continue
            if arr[nx][ny]:
                visited[nx][ny] += 1
                if visited[nx][ny] >= 2:
                    visited[nx][ny] = -1
                    next.append((nx,ny))
            else:
                Q.append((nx,ny))
                visited[nx][ny] = -1
    for x,y in next:
        arr[x][y] = 0
    if next:
        return True
    else:
        return False
        
N, M = map(int, input().rstrip().split())
arr = []
next = []
for i in range(N):
    arr.append(list(map(int, input().rstrip().split())))
    
answer = 0
while True:
    if not bfs():
        print(answer)
        break
    answer += 1