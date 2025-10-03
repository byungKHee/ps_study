dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
WORD = ['d', 'l', 'r', 'u']

def possible(cx,cy,ex,ey,left):
    cnt = abs(cx - ex) + abs(cy-ey)
    if cnt > left or abs(left - cnt) % 2:
        return False
    return True

def solution(n, m, x, y, r, c, k):
    answer = ''
    x-=1
    y-=1
    r-=1
    c-=1
    if not possible(x,y,r,c,k):
        return 'impossible'
    for left in range(k, -1, -1):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny > m:
                continue
            if possible(nx,ny,r,c,left):
                answer += WORD[i]
                x, y = nx, ny
                break

    return answer