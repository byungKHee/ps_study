import sys
from collections import deque
input = sys.stdin.readline

# bfs direction
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def search():
    global keys, answer
    change = False
    visited = [[False] * (M+2) for _ in range(N+2)]
    Q = deque()
    Q.append([0,0])
    visited[0][0] = True
    while Q:
        cx, cy = Q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # range check
            if nx < 0 or nx >= N+2 or ny < 0 or ny >= M+2:
                continue
            # visited check
            if visited[nx][ny]:
                continue
            if arr[nx][ny] == '.':
                Q.append([nx, ny])
                visited[nx][ny] = True
            # target find
            if arr[nx][ny] == '$':
                answer += 1
                arr[nx][ny] = '.'
                change = True
                Q.append([nx,ny])
                visited[nx][ny] = True
            # key find
            elif isKey(nx,ny):
                keys.append(arr[nx][ny])
                arr[nx][ny] = '.'
                change = True
                Q.append([nx,ny])
                visited[nx][ny] = True
            # door find
            elif isDoor(nx,ny):
                if openDoor(nx, ny):
                    arr[nx][ny] = '.'
                    change = True
                    Q.append([nx,ny])
                    visited[nx][ny] = True
    return change

def isDoor(x,y):
    return 65 <= ord(arr[x][y]) <= 90

def openDoor(x,y):
    return chr(ord(arr[x][y]) + 32) in keys

def isKey(x,y):
    return 97 <= ord(arr[x][y]) <= 122

def setParameter():
    global N, M, arr, target, keys
    N, M = map(int, input().split())
    arr = [['.' for _ in range(M+2)] for _ in range(N+2)]
    for i in range(N):
        temp = list(input().rstrip())
        for j in range(M):
            arr[i+1][j+1] = temp[j]
            if arr[i+1][j+1] == '$':
                target.append([i+1, j+1])        
    keys = list(input().rstrip())
    if keys[0] == 0: keys = []

for testCase in range(int(input())):
    # parameter declaration
    N = 0
    M = 0
    arr = []
    keys = []
    target = []
    answer = 0
    # setting parameter
    setParameter()
    # main loop
    while True:
        change = search()
        if not change:
            break
    print(answer)