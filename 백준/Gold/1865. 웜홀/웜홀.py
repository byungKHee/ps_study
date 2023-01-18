import sys
import heapq
input = sys.stdin.readline

def resetDis():
    for i in range(N+1): dis[i] = float("inf")

def func(start):
    dis[start] = 0
    for _ in range(N-1):
        for curr_node in range(0, N+1):
            if dis[curr_node] == float("inf"):
                continue
            for next_node, next_w in graph[curr_node]:
                if dis[curr_node] + next_w < dis[next_node]:
                    dis[next_node] = dis[curr_node] + next_w

def checkCycle():
    for curr_node in range(1, N+1):
        if dis[curr_node] == float("inf"):
            continue
        for next_node, next_w in graph[curr_node]:
            if dis[curr_node] + next_w < dis[next_node]:
                return True
    return False

for T in range(int(input())):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b,w = map(int, input().split())
        graph[a].append((b,w))
        graph[b].append((a,w))
    for _ in range(W):
        a,b,w = map(int, input().split())
        graph[a].append((b,-w))
    dis = [float("inf") for _ in range(N+1)]
    for i in range(1, N+1):
        graph[0].append((i, 0))
    func(0)
    if checkCycle():
        print("YES")
    else:
        print("NO")