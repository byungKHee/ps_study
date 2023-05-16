import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

N, M = map(int, input().split())
arr = []
visited = [[False] * M for _ in range(N)]
Q = deque()
Fire = deque()
for i in range(N):
    arr.append(list(input().rstrip()))
    for j in range(M):
        if arr[i][j] == 'J':
            Q.append([i,j])
        if arr[i][j] == 'F':
            Fire.append([i,j])
            visited[i][j] = True
        if arr[i][j] == '#':
            visited[i][j] = True
answer = 0
while Q:
    answer += 1
    # 1. fire spread
    if Fire:
        tmep_fire = []
        while Fire:
            a,b = Fire.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if visited[nx][ny]:
                    continue
                tmep_fire.append([nx,ny])
                visited[nx][ny] = True
        Fire = deque(tmep_fire)
    # 2. jihoon move
    temp_j = []
    while Q:
        a,b = Q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                print(answer)
                sys.exit()
            if visited[nx][ny]:
                continue
            temp_j.append([nx,ny])
            visited[nx][ny] = True
    Q = deque(temp_j)
print("IMPOSSIBLE")