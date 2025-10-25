from collections import deque
from itertools import permutations

targets = {}
answer = 100000000

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def find_next(board, x, y, tx, ty):
    visited = [[False] * 4 for _ in range(4)]
    visited[x][y] = True
    Q = deque()
    Q.append([x,y,0])
    while Q:
        cx, cy, dis = Q.popleft()
        if cx == tx and cy == ty:
            return dis
        
        for i in range(4):
            # 한칸 이동
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            if visited[nx][ny]:
                continue
            
            Q.append([nx, ny, dis+1])
            visited[nx][ny] = True
            
        for i in range(4):
            # ctrl + 이동
            nx, ny = cx, cy
            while (0 <= nx + dx[i] < 4 and 0 <= ny + dy[i] < 4):
                nx, ny = nx + dx[i], ny + dy[i]
                if board[nx][ny]:
                    break
            if visited[nx][ny]:
                continue
            Q.append([nx, ny, dis+1])
            visited[nx][ny] = True

def bt(board, x, y, order, idx, dis):
    global targets, answer
    
    # 가지치기
    if dis > answer:
        return
    
    target = order[idx]
    loc1 = targets[target][0]
    loc2 = targets[target][1]
    
    # 1 -> 2
    next_dis = find_next(board, x, y, loc1[0], loc1[1]) + find_next(board, loc1[0], loc1[1], loc2[0], loc2[1]) + 2
    
    if idx == len(order) - 1:
        answer = min(answer, dis + next_dis)
        # print(order, dis + next_dis)
    else:
        board[loc1[0]][loc1[1]] = 0
        board[loc2[0]][loc2[1]] = 0
        bt(board, loc2[0], loc2[1], order, idx+1, dis + next_dis)
        board[loc1[0]][loc1[1]] = target
        board[loc2[0]][loc2[1]] = target

    # 2 -> 1
    next_dis = find_next(board, x, y, loc2[0], loc2[1]) + find_next(board, loc2[0], loc2[1], loc1[0], loc1[1]) + 2
    
    if idx == len(order) - 1:
        answer = min(answer, dis + next_dis)
        # print(order, dis + next_dis)
    else:
        board[loc1[0]][loc1[1]] = 0
        board[loc2[0]][loc2[1]] = 0
        bt(board, loc1[0], loc1[1], order, idx+1, dis + next_dis)
        board[loc1[0]][loc1[1]] = target
        board[loc2[0]][loc2[1]] = target


def solution(board, r, c):
    global targets, answer
    targets = {}
    answer = 100000000
    numbers = []
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if board[i][j] not in numbers:
                    numbers.append(board[i][j])
                if board[i][j] not in targets:
                    targets[board[i][j]] = []
                targets[board[i][j]].append([i,j])


    for target in permutations(numbers, len(numbers)):
        bt(board, r, c, list(target), 0, 0)
    
    return answer