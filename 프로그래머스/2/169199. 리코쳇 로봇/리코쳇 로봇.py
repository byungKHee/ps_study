from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(board):
    answer = 0
    visited = [[[False] * 4 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    # 시작위치 찾기
    sx = 0
    sy = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                sx = i
                sy = j
                
    def out(x,y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return True
        return False

    # bfs
    def bfs():
        nonlocal answer
        q = deque()
        q.append([sx, sy, 0, -1])
        while q:
            cx,cy,cnt,prev = q.popleft()
            if board[cx][cy] == 'G':
                answer = cnt
                break
            for i in range(4):
                if prev == i: continue
                if visited[cx][cy][i]: continue
                # 벽이나 D에 닿을 때까지 이동
                visited[cx][cy][i] = True
                nx, ny = cx, cy
                while not out(nx + dx[i], ny + dy[i]) and board[nx + dx[i]][ny + dy[i]] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                q.append([nx,ny,cnt+1, i])
    bfs()
    if answer == 0:
        return -1
    return answer