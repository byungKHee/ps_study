import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def markIsland(x,y,idx):
    visited[x][y] = True
    arr[x][y] = idx
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not visited[nx][ny] and arr[nx][ny]:
            markIsland(nx,ny,idx)

def dis(start):
    start_x, start_y = island[start-1]
    d = [[float('inf')]* N for _ in range(N)]
    d[start_x][start_y] = 0
    Q = []
    heapq.heappush(Q, [0, start_x, start_y])
    while Q:
        count,x,y = heapq.heappop(Q)    
        if d[x][y] < count:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] != start and arr[nx][ny] != 0:
                return count
            if arr[nx][ny] == start and d[nx][ny] != 0:
                d[nx][ny] = 0
                heapq.heappush(Q, [0,nx,ny])
            if arr[nx][ny] == 0 and count+1 < d[nx][ny]:
                d[nx][ny] = count + 1
                heapq.heappush(Q, [count+1,nx,ny])
    return

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
island = []
count = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j]:
            markIsland(i,j,count)
            island.append([i,j])
            count += 1
answer = 2*N
for i in range(1,count):
    answer = min(answer, dis(i))
print(answer)