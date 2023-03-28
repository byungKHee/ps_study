import sys
import heapq
input = sys.stdin.readline

def func(start, graph, dis):
    dis[start] = 0
    Q = []
    heapq.heappush(Q, [0, start])
    while Q:
        curr_w, curr_node = heapq.heappop(Q)
        if dis[curr_node] < curr_w:
            continue
        
        for next_node, next_w in graph[curr_node]:
            if dis[next_node] > curr_w + next_w:
                dis[next_node] = curr_w + next_w
                heapq.heappush(Q, [dis[next_node], next_node])

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
graph_inverse = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,w = map(int, input().split())
    graph[a].append([b,w])
    graph_inverse[b].append([a,w])
dis = [float('inf') for _ in range(N+1)]
dis_inverse = [float('inf') for _ in range(N+1)]
func(X, graph, dis)
func(X, graph_inverse, dis_inverse)
answer = 0
for i in range(1,N+1):
    answer = max(answer, dis[i] + dis_inverse[i])
print(answer)