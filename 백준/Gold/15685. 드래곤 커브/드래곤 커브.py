import sys
input = sys.stdin.readline

# right, up, left, down
dx = [0,-1,0,1]
dy = [1,0,-1,0]

N = int(input())
arr = [[False] * 101 for _ in range(101)]
for _ in range(N):
    y,x,d,g = map(int, input().split())
    move = [d, ]
    for _ in range(g):
        for i in range(len(move)-1, -1, -1):
            move.append((move[i]+1) % 4)
    arr[x][y] = True
    for i in move:
        x += dx[i]
        y += dy[i]
        if (0 <= x <= 100) and (0 <= y <= 100):
            arr[x][y] = True

answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            answer += 1
print(answer)