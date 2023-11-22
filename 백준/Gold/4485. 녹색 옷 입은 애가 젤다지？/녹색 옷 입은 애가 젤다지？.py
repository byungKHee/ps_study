import sys
from heapq import heappop, heappush
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def func(a,b):
    dis[a][b] = arr[a][b]
    Q = [[dis[a][b],a,b]]
    while Q:
        cdis, cx, cy = heappop(Q)
        if cdis > dis[cx][cy]:
            continue
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if cdis + arr[nx][ny] < dis[nx][ny]:
                dis[nx][ny] = cdis + arr[nx][ny]
                heappush(Q, [dis[nx][ny], nx, ny])
                
testCase = 1
while True:
    N = int(input())
    if N == 0: break
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    dis = [[float('inf')] * N for _ in range(N)]
    func(0,0)
    print(f'Problem {testCase}: {dis[N-1][N-1]}')
    testCase += 1