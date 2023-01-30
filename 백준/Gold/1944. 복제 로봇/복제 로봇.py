import sys
from collections import deque
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        root = find(parent[x])
        parent[x] = root
        return root

def union(x,y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[x_root] = y_root
        return True
    return False

def reset():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

def bfs(start_x,start_y):
    count = 0
    reset()
    queue = deque()
    visited[start_x][start_y] = True
    queue.append((start_x,start_y,0))
    while queue:
        x, y, dis = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if maze[nx][ny] == '1' or visited[nx][ny]:
                continue
            if maze[nx][ny] == 'K' or maze[nx][ny] == 'S':
                graph.append((N*start_x+start_y, N*nx+ny, dis+1))
                count += 1
            queue.append((nx, ny, dis+1))
            visited[nx][ny] = True
    return count

dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M = map(int, input().split())
visited = [[False for _ in range(N)] for _ in range(N)]
maze = []
for _ in range(N):
    maze.append(list(input().rstrip()))

start_x,start_y = 0,0
keys = []
for i in range(N):
    for j in range(N):
        if maze[i][j] == 'S':
            start_x, start_y = i,j
        if maze[i][j] == 'K':
            keys.append((i,j))
graph = []
if bfs(start_x, start_y) < len(keys):
    print(-1)
else:
    for x,y in keys:
        bfs(x,y)
    parent = {}
    parent[N*start_x+start_y] = N*start_x+start_y
    for x,y in keys:
        parent[N*x+y] = N*x+y
    count = 0
    answer = 0
    graph.sort(key=lambda x : x[2])
    for x,y,w in graph:
        if union(x,y):
            count += 1
            answer += w
        if count == len(keys):
            break
    print(answer)