import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 1. 그래프 만들기
graph = [[] for _ in range(N*N)]
indegree = [0 for _ in range(N*N)]
for i in range(N):
    for j in range(N):
        curr = i * N + j
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[i][j] >= arr[nx][ny]:
                continue
            curr = i*N + j
            next = nx*N + ny
            graph[curr].append(next)
            indegree[next] += 1

# 2. 위상정렬 + dp
dp = [1 for _ in range(N*N)]
Q = deque()
for node in range(N*N):
    if not indegree[node]:
        Q.append(node)

answer = 1
while Q:
    curr = Q.popleft()
    for next in graph[curr]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[curr] + 1)
        if indegree[next] == 0:
            Q.append(next)
print(max(dp))