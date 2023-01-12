import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [[[False] * 2 for _ in range(M)] for __ in range(N)]
    visited[0][0][1] = True
    queue = deque([(0,0,1,1), ])
    while queue:
        curr = queue.popleft()
        if curr[0] == N-1 and curr[1] == M-1:
            return curr[3]
        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]
            bomb = curr[2]
            count = curr[3]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if bomb:
                if maze[nx][ny] == 1 and not visited[nx][ny][bomb-1]:
                    queue.append((nx,ny,bomb-1,count+1))
                    visited[nx][ny][bomb-1] = True
                if maze[nx][ny] == 0 and not visited[nx][ny][bomb]:
                    queue.append((nx,ny,bomb,count+1))
                    visited[nx][ny][bomb] = True
            else:
                if visited[nx][ny][bomb]:
                    continue
                if maze[nx][ny] == 1:
                    continue
                queue.append((nx,ny,bomb,count+1))
                visited[nx][ny][bomb] = True
    return -1
        
N, M = map(int, input().rstrip().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

print(bfs())