import sys
from collections import deque
input = sys.stdin.readline

dn = [1,-1,0,0,0,0]
dm = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1]
def bfs():
    global answer
    while Q:
        h,n,m,date = Q.popleft()
        answer = max(answer, date)
        for i in range(6):
            nh = h + dh[i]
            nn = n + dn[i]
            nm = m + dm[i]
            if nh < 0 or nh >= H or nn < 0 or nn >= N or nm < 0 or nm >= M:
                continue
            if not visited[nh][nn][nm] and arr[nh][nn][nm] == 0:
                Q.append([nh,nn,nm,date+1])
                visited[nh][nn][nm] = True


def check():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if not visited[h][n][m] and arr[h][n][m] == 0:
                    return False
    return True 

answer = 0
M, N, H = map(int, input().split())
arr = [[] for _ in range(H)]
for h in range(H):
    for n in range(N):
        arr[h].append(list(map(int, input().split())))
visited = [[[False] * M for n in range(N)] for h in range(H)]
Q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1:
                Q.append([h,n,m,0])
                visited[h][n][m] = True
bfs()
if check():
    print(answer)
else:
    print(-1)