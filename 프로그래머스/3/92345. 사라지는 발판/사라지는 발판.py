from copy import deepcopy
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def func(visited, ax, ay, bx, by, turn):
    # A턴
    if not turn % 2:
        if visited[ax][ay]:
            return [False, turn]
        result = []
        for i in range(4):
            nx, ny = ax + dx[i], ay + dy[i]
            if nx < 0 or nx >= len(visited) or ny < 0 or ny >= len(visited[0]):
                result.append([False, turn])
                continue
            if visited[nx][ny]:
                result.append([False, turn])
                continue
            next = deepcopy(visited)
            next[ax][ay] = True
            result.append(func(next, nx, ny, bx, by, turn + 1))
        # 하나라도 이긴다면 최소시간, 모두 진다면 최대기간
        if any([a[0] for a in result]): # 이긴거 하나 이상 있음
            return [True, min([a[1] for a in result if a[0]])]
        else:
            return [False, max([a[1] for a in result])] # 다 짐
    if turn % 2:
        if visited[bx][by]:
            return [True, turn]
        result = []
        for i in range(4):
            nx, ny = bx + dx[i], by + dy[i]
            if nx < 0 or nx >= len(visited) or ny < 0 or ny >= len(visited[0]):
                result.append([True, turn])
                continue
            if visited[nx][ny]:
                result.append([True, turn])
                continue
            next = deepcopy(visited)
            next[bx][by] = True
            result.append(func(next, ax, ay, nx, ny, turn + 1))
            
        if all([a[0] for a in result]):
            return [True, max([a[1] for a in result])] # 다 짐
        else:
            return [False, min([a[1] for a in result if not a[0]])] # 하나라도 이긴 거 있음
            
def solution(board, aloc, bloc):
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited[i][j] = not board[i][j]
    A_win, answer = func(visited, aloc[0], aloc[1], bloc[0], bloc[1], 0)
    print(A_win, answer)
    return answer