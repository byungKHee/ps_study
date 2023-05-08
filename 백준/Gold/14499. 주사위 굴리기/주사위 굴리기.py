import sys
from collections import deque
input = sys.stdin.readline

# top, north, east, south, west, bottom
def roll(direction):
    if direction == 1:
        temp = dice[0]
        dice[0] = dice[4]   # west -> top
        dice[4] = dice[5]   # bottom -> west
        dice[5] = dice[2]   # east -> bottom
        dice[2] = temp      # top -> east
    elif direction == 2:
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp
    elif direction == 3:
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
    else:
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
    if not arr[x][y]:
        arr[x][y] = dice[-1]
    else:
        dice[-1] = arr[x][y]
        arr[x][y] = 0
def printDice():
    print(f' {dice[0]}')
    print(f' {dice[1]}')
    print(f'{dice[4]}{dice[-1]}{dice[2]}')
    print(f' {dice[3]}')
    print()
    
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

dice = [0] * 6
N, M, x, y, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
order = list(map(int, input().split()))
dice[-1] = arr[x][y]
arr[x][y] = 0
for i in order:
    # printDice()
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    x,y = nx, ny
    roll(i)
    print(dice[0])
