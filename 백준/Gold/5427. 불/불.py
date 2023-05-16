import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for testCase in range(int(input())):
    M, N = map(int, input().split())
    arr = []
    visited = [[False] * M for _ in range(N)]
    Q = deque()
    Fire = deque()
    for i in range(N):
        arr.append(list(input().rstrip()))
        for j in range(M):
            if arr[i][j] == '@':
                Q.append([i,j])
            if arr[i][j] == '*':
                Fire.append([i,j])
                visited[i][j] = True
            if arr[i][j] == '#':
                visited[i][j] = True
    escape = False
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
                    escape = True
                    break
                if visited[nx][ny]:
                    continue
                temp_j.append([nx,ny])
                visited[nx][ny] = True
        if escape:
            break
        Q = deque(temp_j)
    if escape:
        print(answer)
    else:
        print("IMPOSSIBLE")