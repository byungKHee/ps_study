import sys
from collections import deque
input = sys.stdin.readline

def CtoD(c):
    return ord(c) - ord('A')

dx = [1,-1,0,0]
dy = [0,0,1,-1]    
def dfs(curr, visited, count):
    global answer
    visited[CtoD(arr[curr[0]][curr[1]])] = True
    count += 1
    answer = max(answer, count)
    for i in range(4):
        nx = curr[0] + dx[i]
        ny = curr[1] + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[CtoD(arr[nx][ny])]:
            continue
        dfs((nx,ny), visited[:], count)

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(input().rstrip()))
answer = 0
temp = [False for i in range(26)]
dfs((0,0), temp, 0)
print(answer)