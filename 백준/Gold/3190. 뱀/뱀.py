import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    x,y = map(int, input().split())
    arr[x-1][y-1] = 1
L = int(input())
D = {}
for _ in range(L):
    a,b = input().rstrip().split()
    if b == 'L':
        D[int(a)] = -1
    else:
        D[int(a)] = 1
t = 0
direction = 0
body = deque()
body.append([0,0])
while True:
    # print(t)
    # for i in range(N):
    #     for j in range(N):
    #         if [i,j] in body:
    #             if i == body[0][0] and j == body[0][1]:
    #                 print('h', end = '')
    #             else:
    #                 print('x',end = '')
    #         else:
    #             print(arr[i][j], end = '')
    #     print()
    # print()
    t += 1
    if t-1 in D:
        direction = (direction + D[t-1]) % 4
    nx = body[0][0] + dx[direction]
    ny = body[0][1] + dy[direction]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break
    if [nx, ny] in body:
        break
    body.appendleft([nx,ny])
    if arr[nx][ny]:
        arr[nx][ny] = 0
    else:
        body.pop()
print(t)