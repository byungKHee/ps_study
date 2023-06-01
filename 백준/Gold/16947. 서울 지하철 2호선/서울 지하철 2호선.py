import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def findCycle(prev, curr):
    flag = 0
    visited[curr] = True
    for next in graph[curr]:
        if next == prev:
            continue
        if not visited[next]:
            flag = findCycle(curr, next)
        elif not finished[next]:
            flag = next
        if flag:
            break
    cycle[curr] = bool(flag)
    finished[curr] = True
    if curr == flag:
        return 0
    return flag

def bfs(start):
    for i in range(N+1):
        visited[i] = False
    dis[start] = 0
    Q = deque()
    Q.append([start, 0])
    visited[start] = True
    while Q:
        curr, d = Q.popleft()
        dis[curr] = d
        for next in graph[curr]:
            if visited[next]:
                continue
            if cycle[next]:
                Q.append([next, d])
                visited[next] = True
            else:
                Q.append([next, d+1])
                visited[next] = True           

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
finished = [False] * (N+1)
cycle = [False] * (N+1)
dis = [0] * (N+1)

findCycle(1,1)
for i in range(1, N+1):
    if cycle[i]:
        bfs(i)
        break
print(*dis[1:])