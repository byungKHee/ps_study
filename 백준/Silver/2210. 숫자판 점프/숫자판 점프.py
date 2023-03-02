import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
arr = []
Q = deque()
answer = []
for _ in range(5):
    arr.append(list(input().split()))
for i in range(5):
    for j in range(5):
        Q.append([(i,j), arr[i][j]])
while Q:
    pos, num = Q.popleft()
    for i in range(4):
        nx = pos[0] + dx[i]
        ny = pos[1] + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if len(num) == 5:
            if num+arr[nx][ny] not in answer:
                answer.append(num+arr[nx][ny])
                continue
            else:
                continue
        Q.append([(nx,ny), num+arr[nx][ny]])
print(len(answer))