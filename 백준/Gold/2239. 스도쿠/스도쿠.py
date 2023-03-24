import sys
input = sys.stdin.readline

box = [[0] * 9 for _ in range(9)]
row = [[0] * 9 for _ in range(9)]
column = [[0] * 9 for _ in range(9)]

def on(x, y, n):
    arr[x][y] = n+1
    row[x][n] = 1
    column[y][n] = 1
    box[(x//3)*3 + y//3][n] = 1

def off(x, y, n):
    arr[x][y] = 0
    row[x][n] = 0
    column[y][n] = 0
    box[(x//3)*3 + y//3][n] = 0

def func(curr):
    if curr == 81:
        return True
    x = curr // 9
    y = curr % 9
    if arr[x][y]:
        return func(curr+1)
    clear = False
    for n in range(9):
        if not row[x][n] and not column[y][n] and not box[(x//3)*3 + y//3][n]:
            on(x,y,n)
            if func(curr+1):
                clear = True
                break
            else:
                off(x,y,n)
                continue
    return clear

arr = []
for _ in range(9):
    arr.append(list(map(int, list(input().rstrip()))))
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            continue
        row[i][arr[i][j]-1] = 1
        column[j][arr[i][j]-1] = 1
        box[(i//3)*3 + j//3][arr[i][j]-1] = 1

func(0)
for r in arr:
    for n in r:
        print(n, end='')
    print()