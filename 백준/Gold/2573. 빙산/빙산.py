import sys
import copy
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def melt():
    global arr
    rnt = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                continue
            for k in range(4):
                cx = i + dx[k]
                cy = j + dy[k]
                if cx < 0 or cx >= N or cy < 0 or cy >= M:
                    continue
                if not arr[cx][cy] and rnt[i][j]:
                    rnt[i][j] -= 1
    arr = rnt

def component():
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                visited[i][j] = False
            else:
                visited[i][j] = True
    count = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                dfs(i,j)
                count += 1
    return count

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if cx < 0 or cx >= N or cy < 0 or cy >= M:
            continue
        if visited[cx][cy]:
            continue
        dfs(cx,cy)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
answer = 0
while True:
    comp = component()
    if comp >= 2:
        print(answer)
        break
    if comp == 0:
        print(0)
        break
    melt()
    answer += 1