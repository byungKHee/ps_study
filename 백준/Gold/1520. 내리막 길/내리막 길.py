import sys
import heapq
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1
visited = [[False] * M for _ in range(N)]
Q = [[-arr[0][0], 0, 0]]

while Q:
    height, x, y = heapq.heappop(Q)
    if visited[x][y]:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if arr[nx][ny] < -height:
            dp[nx][ny] += dp[x][y]
            heapq.heappush(Q, [-arr[nx][ny], nx, ny])
    visited[x][y] = True
print(dp[-1][-1])