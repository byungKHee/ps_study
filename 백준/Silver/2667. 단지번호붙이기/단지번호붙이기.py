import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global count
    count += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if arr[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, list(input().rstrip()))))
visited = [[False for _ in range(N)] for _ in range(N)]
answer = []
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            count = 0
            dfs(i, j)
            answer.append(count)
answer.sort()
print(len(answer))
for i in answer: print(i)