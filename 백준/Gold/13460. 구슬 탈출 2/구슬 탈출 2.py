import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def move(redX, redY, blueX, blueY, direction):
    rx, ry, bx, by = redX, redY, blueX, blueY
    while True:
        if arr[rx + dx[direction]][ry + dy[direction]] == '#':
            break
        rx += dx[direction]
        ry += dy[direction]
        if arr[rx][ry] == 'O':
            break
    while True:
        if arr[bx + dx[direction]][by + dy[direction]] == '#':
            break
        bx += dx[direction]
        by += dy[direction]
        if arr[bx][by] == 'O':
            break
    if not (rx == bx and ry == by):
        return rx, ry, bx, by
    else:
        if rx == targetX and ry == targetY:
            return rx, ry, bx, by
        else:
            if direction == 0: # up
                if redX < blueX:
                    bx += 1
                else:
                    rx += 1
            elif direction == 1: # down
                if redX < blueX:
                    rx -= 1
                else:
                    bx -= 1
            elif direction == 2:
                if redY < blueY:
                    ry -= 1
                else:
                    by -= 1
            else:
                if redY < blueY:
                    by += 1
                else:
                    ry += 1
            return rx, ry, bx, by


N, M = map(int, input().split())
arr = []
rx, ry, bx, by = 0, 0, 0, 0
targetX, targetY = 0, 0
for i in range(N):
    arr.append(list(input().rstrip()))
    for j in range(M):
        if arr[i][j] == 'R':
            rx, ry = i,j
        if arr[i][j] == 'B':
            bx, by = i,j
        if arr[i][j] == 'O':
            targetX, targetY = i,j

visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
Q = deque()
Q.append([rx, ry, bx, by, 0])
visited[rx][ry][bx][by] = True
answer = 0
flag = False
while Q:
    currRedX, currRedY, currBlueX, currBlueY, count = Q.popleft()
    if count >= 10:
        break
    for i in range(4):
        nextRedX, nextRedY, nextBlueX, nextBlueY = move(currRedX, currRedY, currBlueX, currBlueY, i)
        if visited[nextRedX][nextRedY][nextBlueX][nextBlueY]:
            continue
        if nextBlueX == targetX and nextBlueY == targetY:
            visited[nextRedX][nextRedY][nextBlueX][nextBlueY] = True
            continue
        if nextRedX == targetX and nextRedY == targetY:
            answer = count + 1
            flag = True
            break
        Q.append([nextRedX, nextRedY, nextBlueX, nextBlueY, count+1])
        visited[nextRedX][nextRedY][nextBlueX][nextBlueY] = True
    if flag:
        break
if not flag:
    print(-1)
else:
    print(answer)