from collections import deque

dx = (1,-1,0,0)
dy = (0,0,1,-1)
def solution(maps):
    answer = -1
    Q = deque()
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    Q.append([0,0,1])
    visited[0][0] = True
    while Q:
        cx, cy, dis = Q.popleft()
        if cx == len(maps)-1 and cy == len(maps[0])-1:
            answer = dis
            break
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0 or visited[nx][ny]:
                continue
            Q.append([nx,ny,dis+1])
            visited[nx][ny] = True
    return answer