import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,px,py,count,total):
    global answer
    if count == 4:
        answer = max(answer, total + arr[x][y])
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if nx == px and ny == py:
            continue
        dfs(nx, ny, x, y, count+1, total+arr[x][y])

def func(x,y):
    global answer
    for i in range(4):
        total = arr[x][y]
        for k in range(4):
            if k == i:
                continue
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            total += arr[nx][ny]
        answer = max(answer, total)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
answer = 0
for i in range(N):
    for j in range(M):
        func(i,j)
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            dfs(nx,ny,i,j,2,arr[i][j])
print(answer)