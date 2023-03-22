import sys
from collections import deque
input = sys.stdin.readline

def reset_visited(a,b,c):
    for i in range(size):
        visited[i] = False
    visited[a] = True
    visited[b] = True
    visited[c] = True

def safe_count():
    count = 0
    for i in range(size):
        if not visited[i]: 
            count += 1
    return count

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int, input().split())
size = N*M
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

node = [[0]*M for _ in range(N)]
virus = []
wall = []
graph = [[] for i in range(size)]
for i in range(N):
    for j in range(M):
        # node num setting
        node[i][j] = i*M+j

        # virus location
        if arr[i][j] == 2:
            virus.append(i*M+j)

        # wall location
        if arr[i][j] == 1:
            wall.append(i*M+j)

        # graph setting
        for k in range(4):
            cx = i + dx[k]
            cy = j + dy[k]
            if cx < 0 or cx >= N or cy < 0 or cy >= M:
                continue
            if arr[cx][cy] != 1:
                graph[i*M+j].append(cx*M+cy)
answer = 0
visited = [False for _ in range(size)]
for i in range(size-2):
    if i in virus or i in wall: continue
    for j in range(i+1, size-1):
        if j in virus or j in wall: continue
        for k in range(j+1, size):
            if k in virus or k in wall: continue
            reset_visited(i,j,k)
            Q = deque()
            for v in virus:
                Q.append(v)
                visited[v] = True
            while Q:
                curr = Q.popleft()
                for next in graph[curr]:
                    if not visited[next]:
                        Q.append(next)
                        visited[next] = True
            answer = max(answer, safe_count())
print(answer-len(wall))