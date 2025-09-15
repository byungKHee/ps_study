from collections import deque
def solution(land):
    N = len(land)
    M = len(land[0])
    total = [0] * M
    visited = [[0] * M for _ in range(N)]
    
    count = {}
    component = 1
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def bfs(x,y):
        rnt = 0
        Q = deque()
        Q.append([x,y])
        visited[x][y] = component
        while Q:
            cx, cy = Q.popleft()
            rnt += 1
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if visited[nx][ny]:
                    continue
                if not land[nx][ny]:
                    continue
                Q.append([nx,ny])
                visited[nx][ny] = component
        return rnt
    
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and visited[i][j] == 0:
                rnt = bfs(i,j)
                count[component] = rnt
                component += 1
    for j in range(M):
        visit = [False] * component
        for i in range(N):
            component_num = visited[i][j]
            if component_num != 0 and not visit[component_num]:
                total[j] += count[component_num]
                visit[component_num] = True
        
    return max(total)