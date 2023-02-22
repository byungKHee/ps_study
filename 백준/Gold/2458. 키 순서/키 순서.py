import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
dis = [[float('inf') for i in range(N)] for i in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    dis[a-1][b-1] = 0
for i in range(N):
    dis[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
answer = N
for i in range(N):
    for j in range(N):
        if dis[i][j] and dis[j][i]:
            answer -= 1
            break
print(answer)