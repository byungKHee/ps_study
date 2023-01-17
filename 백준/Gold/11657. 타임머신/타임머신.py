import sys
import heapq
input = sys.stdin.readline

def func(start):
    dis[start] = 0
    for i in range(N-1):
        for curr_node in range(1,N+1):
            for next_node, next_dis in graph[curr_node]:
                if dis[curr_node] + next_dis < dis[next_node]:
                    dis[next_node] = dis[curr_node] + next_dis

def checkCycle():
    for curr_node in range(1,N+1):
        for next_node, next_dis in graph[curr_node]:
            if dis[curr_node] + next_dis < dis[next_node]:
                return True
    return False

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
dis = [float("inf") for _ in range(N+1)]
func(1)
if checkCycle():
    print(-1)
else:
    for i in range(2, N+1):
        if dis[i] == float("inf"): print(-1)
        else: print(dis[i])