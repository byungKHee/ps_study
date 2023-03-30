import sys
from collections import deque
input = sys.stdin.readline

def func(start):
    dis[start] = profit[start]
    cycle_node = []
    for _ in range(N-1):
        for curr_node in range(N):
            for next_node, next_w in graph[curr_node]:
                if dis[curr_node] + next_w > dis[next_node]:
                    dis[next_node] = dis[curr_node] + next_w
    for curr_node in range(N):
        for next_node, next_w in graph[curr_node]:
            if dis[curr_node] + next_w > dis[next_node]:
                if curr_node not in cycle_node:
                    cycle_node.append(curr_node)
    return cycle_node

N, start, end, M = map(int, input().split())
graph = [[] for _ in range(N)]
dis = [float('-inf') for i in range(N)]
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))
profit = list(map(int, input().split()))
for a,b,w in edges:
    graph[a].append((b, -w+profit[b]))

cycle_node = func(start)
if dis[end] == float('-inf'):
    print("gg")
else:
    if not cycle_node:
        print(dis[end])
    else:
        visited = [False for _ in range(N)]
        Q = deque()
        for node in cycle_node:
            visited[node] = True
            Q.append(node)
        while Q:
            curr = Q.popleft()
            for next, w in graph[curr]:
                if not visited[next]:
                    Q.append(next)
                    visited[next] = True
                    if visited[end]:
                        break
        if visited[end]:
            print("Gee")
        else:
            print(dis[end])