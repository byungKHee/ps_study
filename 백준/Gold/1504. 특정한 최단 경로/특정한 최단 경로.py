import sys
import math
import heapq
input = sys.stdin.readline

def resetDis():
    for i in range(N+1):
        dis[i] = float("inf")

def func(start, end):
    resetDis()
    dis[start] = 0
    Q = [(0, start)]
    while Q:
        curr_dis, curr_node = heapq.heappop(Q)
        if curr_dis > dis[curr_node]:
            continue
        for next_node, next_w in graph[curr_node]:
            if curr_dis + next_w < dis[next_node]:
                dis[next_node] = curr_dis + next_w
                heapq.heappush(Q, (dis[next_node], next_node))
    return dis[end]

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis = [float('inf') for _ in range(N+1)]
for _ in range(E):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
v1, v2 = map(int, input().split())

mid = func(v1, v2)
a = func(1, v1) + mid + func(v2, N)
b = func(1, v2) + mid + func(v1, N)
if a == float('inf') and b == float('inf'):
    print(-1)
else:
    print(min(a,b))