import sys
import heapq
input = sys.stdin.readline

def func(start, des):
    dis = [float("inf") for _ in range(size)]
    dis[start] = 0
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        curr_dis, curr_node = heapq.heappop(queue)
        if dis[curr_node] < curr_dis:
            continue
        for next_node, next_w in graph[curr_node]:
            if curr_dis + next_w < dis[next_node]:
                dis[next_node] = curr_dis + next_w
                heapq.heappush(queue, (curr_dis + next_w, next_node))

    return dis[des]
    
N, K = map(int, input().rstrip().split())
size = (4*max(K,N)) // 3 + 1
graph = [[] for _ in range(size)]
for i in range(size):
    if i-1 >= 0:
        graph[i].append((i-1,1))
    if i+1 < size:
        graph[i].append((i+1,1))
    if 2*i < size:
        graph[i].append((2*i,0))

print(func(N,K))