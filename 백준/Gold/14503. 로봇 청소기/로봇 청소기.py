import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def clean():
    global arr, answer
    arr[r][c] = 2
    answer += 1

def check():
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not arr[nx][ny]:
            return True
    return False

N, M = map(int, input().split())
r, c, direction = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

answer = 0
while True:
    if not arr[r][c]:
        clean()
    if check():
        for i in range(4):
            direction = (direction - 1) % 4
            nx = r + dx[direction]
            ny = c + dy[direction]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not arr[nx][ny]:
                r = nx
                c = ny
                break
    else:
        nx = r - dx[direction]
        ny = c - dy[direction]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        if arr[nx][ny] == 1:
            break
        r = nx
        c = ny
print(answer)