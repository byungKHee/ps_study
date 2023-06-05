import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(curr):
    visited[curr] = True
    query[curr] = 1
    for child in graph[curr]:
        if visited[child]:
            continue
        dfs(child)
        query[curr] += query[child]

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
query = [0] * (N+1)
visited = [False] * (N+1)
dfs(R)
for _ in range(Q):
    print(query[int(input())])