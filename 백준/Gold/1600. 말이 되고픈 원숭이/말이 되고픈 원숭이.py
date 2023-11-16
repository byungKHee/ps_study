import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
M, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
visited = [[[False] * M for _ in range(N)] for _ in range(K+1)]

dx = [1,-1,0,0,1,2,2,1,-1,-2,-2,-1]
dy = [0,0,1,-1,2,1,-1,-2,-2,-1,1,2]

answer = -1
Q = deque()
Q.append([0,0,0,0])
visited[0][0][0] = True
while Q:
    cx,cy,k_count,dis = Q.popleft()
    if cx == N-1 and cy == M-1:
        answer = dis
        break
    for i in range(12):
        if i < 4:
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[k_count][nx][ny] or arr[nx][ny]:
                continue
            Q.append([nx,ny,k_count,dis+1])
            visited[k_count][nx][ny] = True
        else:
            if k_count >= K:
                break
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[k_count+1][nx][ny] or arr[nx][ny]:
                continue
            Q.append([nx,ny,k_count+1,dis+1])
            visited[k_count+1][nx][ny] = True
print(answer)