import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    for i in range(N+1):
        visited[i] = False
    visited[S] = True
    Q = deque()
    Q.append(S)
    while Q:
        curr = Q.popleft()
        for next, cost in graph[curr]:
            if cost < mid or visited[next]:
                continue
            if next == E:
                return True
            Q.append(next)
            visited[next] = True
    return visited[E]

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,w = map(int, input().split())
    graph[a].append([b,w])
    graph[b].append([a,w])
S, E = map(int, input().split())

visited = [False for _ in range(N+1)]
L, R = 0, max([a[1] for a in graph[S]]) + 1
mid = 0
while L+1 < R:
    mid = (L + R) // 2
    if bfs():
        L = mid
    else:
        R = mid
print(L)