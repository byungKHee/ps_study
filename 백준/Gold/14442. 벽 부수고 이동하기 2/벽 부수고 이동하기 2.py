import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N, M, K = map(int, input().split())
arr = []
visited = [[[False] * M for _ in range(N)] for _ in range(K+1)]
for _ in range(N):
    arr.append(list(map(int, list(input().rstrip()))))

Q = deque()
Q.append([0,0,0,1])
visited[0][0][0] = True
answer = -1
while Q:
    cx, cy, ck, dis = Q.popleft()
    if cx == N-1 and cy == M-1:
        answer = dis
        break
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if arr[nx][ny] == 0 and not visited[ck][nx][ny]:
            Q.append([nx,ny,ck,dis+1])
            visited[ck][nx][ny] = True
        if arr[nx][ny] == 1 and ck < K and not visited[ck+1][nx][ny]:
            Q.append([nx,ny,ck+1,dis+1])
            visited[ck+1][nx][ny] = True
print(answer)