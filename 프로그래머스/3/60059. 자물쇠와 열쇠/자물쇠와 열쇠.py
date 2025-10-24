from copy import deepcopy
N = 0
M = 0
SIZE = 0

def possible(target):
    global N, M
    for i in range(N):
        for j in range(N):
            if target[i + M - 1][j + M - 1] != 1:
                return False
    return True

def find(key, target):
    global N, M
    for i in range(N+M-1):
        for j in range(N+M-1):
            temp = deepcopy(target)
            for x in range(M):
                for y in range(M):
                    temp[x + i][y + j] += key[x][y]
            
            if possible(temp):
                return True
    return False
    


# 90도 회전
def turn(arr):
    return [list(row) for row in zip(*arr[::-1])]
    
# # 뒤집기
# def flip(arr):
#     temp = [[0] * len(arr) for _ in range(len(arr))]
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             temp[len(arr) - 1 - i][j] = arr[i][j]
#     return temp
    
def solution(key, lock):
    global N, M
    N = len(lock)
    M = len(key)
    SIZE = N + (M-1) * 2
    arr = [[0] * SIZE for _ in range(SIZE)]
    
    for i in range(N):
        for j in range(N):
            arr[i + M - 1][j + M - 1] = lock[i][j]
    
    # 90도씩 회전
    for i in range(4):
        arr = turn(arr)
        if find(key, arr):
            return True
    
    # arr = flip(arr)
    # for i in range(4):
    #     arr = turn(arr)
    #     if find(key, arr):
    #         return True
    
    return False