import sys
input = sys.stdin.readline

def check(a,b, target, direction):
    if direction == 0:  # 세로 컷 체크
        for i in range(a, b):
            if arr[i][target] == 2:
                return False
    if direction == 1:  # 가로 컷 체크
        for i in range(a,b):
            if arr[target][i] == 2:
                return False
    return True
            

def func(x1, y1, x2, y2, prev):
    if x1 >= x2 or y1 >= y2:
        return 0
    gold = []
    stone = []
    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[i][j] == 1:
                stone.append((i,j))
            if arr[i][j] == 2:
                gold.append((i,j))
    if len(gold) == 1:
        if len(stone) == 0:
            return 1
        else:
            return 0
    if len(gold) == 0:
        return 0
    else:
        if len(stone) == 0:
            return 0
        else:
            count = 0
            # recursion process
            for x,y in stone:
                if prev == 0: # 이전에 세로로 자름
                    if check(y1, y2, x, 1): # 가로 컷 가능한지 체크
                        up = func(x1, y1, x, y2, 1)
                        down = func(x+1, y1, x2, y2, 1)
                        if up and down:
                            count += up*down
                else:   # 이전에 가로로 자름
                    if check(x1, x2, y, 0):
                        left = func(x1, y1, x2, y, 0)
                        right = func(x1, y+1, x2, y2, 0)
                        if left and right:
                            count += left*right
            return count

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
answer = func(0,0,N,N,0) + func(0,0,N,N,1)
if answer:
    print(answer)
else:
    print(-1)