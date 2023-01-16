import sys
import heapq
input = sys.stdin.readline

def func(start, des):
    dis = [float("inf") for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    dis[start] = 0
    visited[start] = True
    queue = []
    queue.append((0,start))
    while queue:
        curr_dis, curr_node = heapq.heappop(queue)
        visited[curr_node] = True
        if dis[curr_node] < curr_dis:
            continue
        for next_node, next_w in graph[curr_node]:
            if visited[next_node]:
                continue
            if curr_dis + next_w < dis[next_node]:
                dis[next_node] = curr_dis + next_w
                heapq.heappush(queue, (dis[next_node], next_node))
    return dis[des]

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,w = map(int, input().rstrip().split())
    graph[a].append((b,w))
start , des = map(int, input().rstrip().split())
print(func(start,des))