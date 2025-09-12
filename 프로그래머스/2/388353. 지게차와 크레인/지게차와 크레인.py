from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def solution(storage, requests):
    answer = len(storage)*len(storage[0])
    arr = [[0] * (len(storage[0]) + 2) for i in range(len(storage) + 2)]
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            arr[i+1][j+1] = storage[i][j]
    
    def bfs(target):
        visited = [[False] * len(arr[0]) for _ in range(len(arr))]
        visited[0][0] = True
        Q = deque()
        Q.append([0,0])
        while Q:
            cx, cy = Q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if nx < 0 or nx >= len(arr) or ny < 0 or ny >=len(arr[0]):
                    continue
                if visited[nx][ny]:
                    continue
                if arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    Q.append([nx,ny])
                elif arr[nx][ny] == target:
                    arr[nx][ny] = 0
                    visited[nx][ny] = True
                
                    
    def findAll(target):
        for i in range(len(storage)):
            for j in range(len(storage[0])):
                if arr[i+1][j+1] == target:
                    arr[i+1][j+1] = 0
    
    # main
    for request in requests:
        if len(request) == 1:
            bfs(request)
        else:
            findAll(request[0])
    
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if arr[i+1][j+1] == 0:
                answer -= 1
                
    return answer