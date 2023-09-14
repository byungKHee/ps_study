import sys
input = sys.stdin.readline

dx = [1,1,0,0]
dy = [1,0,1,0]

def func(x,y,size):
    global blue, white
    if size == 1:
        if arr[x][y] == 1:
            blue += 1
        else:
            white += 1
        return
    complete = True
    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0: continue
            if arr[x][y] != arr[x+i][y+j]:
                complete = False
                break
    if complete:
        if arr[x][y] == 1:
            blue += 1
        else:
            white += 1
    else:
        dis = size // 2
        for i in range(4):
            func(x + dis*dx[i], y + dis*dy[i], dis)

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
    
blue = 0
white = 0
func(0,0,N)
print(white)
print(blue)