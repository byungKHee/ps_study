import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(sx, sy, id, arr):
    q = deque()
    q.append([sx, sy])
    arr[sx][sy] = id
    cnt = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny]:
                continue
            arr[nx][ny] = id
            cnt += 1
            q.append([nx,ny])
    return cnt
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, list(input().rstrip()))))

component = {}
answer = []
for a in arr:
    answer.append(a[:])

id = 2
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            cnt = bfs(i,j,id,arr)
            component[id] = cnt
            id += 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            near = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if arr[nx][ny] not in component:
                    continue
                near.add(arr[nx][ny])
            cnt = 1
            for n in near:
                cnt += component[n]                
            answer[i][j] = cnt
for a in answer:
    print("".join(map(lambda x : str(x % 10), a)))
