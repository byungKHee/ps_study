import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dis[start] = 0
    queue = [(0,start), ]
    while queue:
        curr_dis, curr_node = heapq.heappop(queue)
        if curr_dis > dis[curr_node]:
            continue
        for next_node, next_w in graph[curr_node]:
            if next_w + curr_dis < dis[next_node]:
                dis[next_node] = next_w + curr_dis
                heapq.heappush(queue, (dis[next_node], next_node))

M, N = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
size = N * M
graph = [[] for _ in range(size)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(N):
    for j in range(M):
        for k in range(4):
            x = i+dx[k]
            y = j+dy[k]
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if maze[x][y] == 1:
                graph[M*i+j].append((M*x+y, 1))
            else:
                graph[M*i+j].append((M*x+y, 0))
dis = [float("inf") for _ in range(size)]
dijkstra(0)
if dis[size-1] == float("inf"):
    print(0)
else:
    print(dis[size-1])