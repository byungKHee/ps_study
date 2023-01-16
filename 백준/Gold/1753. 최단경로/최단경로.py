import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dis[start] = 0
    queue = []
    queue.append((0,start))
    while queue:
        curr_dis, curr_node = heapq.heappop(queue)
        if curr_dis > dis[curr_node]:
            continue
        for next_node, next_w in graph[curr_node]:
            if dis[curr_node] + next_w < dis[next_node]:
                dis[next_node] = dis[curr_node] + next_w
                heapq.heappush(queue, (dis[next_node], next_node))

V, E = map(int, input().rstrip().split())
start = int(input())
graph = [[] for _ in range(V+1)]
dis = [float("inf") for _ in range(V+1)]
for _ in range(E):
    a,b,w = map(int, input().rstrip().split())
    graph[a].append((b,w))
dijkstra(start)
for i in range(1, V+1):
    if dis[i] == float("+inf"):
        print("INF")
    else:
        print(dis[i])