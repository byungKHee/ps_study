import sys
from collections import deque
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def isCycle(start, curr, count):
    global flag
    visited[curr] = True
    for next in graph[curr]:
        if flag:
            break
        if not visited[next]:
            isCycle(start, next, count+1)
        elif count > 2 and start == next:
            flag = True

def bfs(start):
    Q = deque()
    Q.append(start)
    visited[start] = True
    while Q:
        curr = Q.popleft()
        for next in graph[curr]:
            if visited[next]:
                continue
            Q.append(next)
            visited[next] = True
            if not cycle[next]:
                dis[next] = dis[curr] + 1

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
cycle = [False] * (N+1)
dis = [0] * (N+1)

# dfs: find cycle
for node in range(1, N+1):
    for i in range(N+1):
        visited[i] = False
    flag = False
    isCycle(node, node, 1)
    if flag:
        cycle[node] = True

# bfs: find dis from cycle
for node in range(1, N+1):
    if cycle[node]:
        for i in range(N+1):
            visited[i] = False
        bfs(node)
        break

# print answer
print(*dis[1:])