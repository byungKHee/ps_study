import sys
from collections import deque
input = sys.stdin.readline

def topological_sort():
    sorted_arr = []
    Q = deque()
    for i in range(N):
        if indegree[i] == 0:
            Q.append(i)
    while Q:
        curr = Q.popleft()
        sorted_arr.append(curr)
        for next in graph[curr]:
            indegree[next] -= 1
            if indegree[next] == 0:
                Q.append(next)
    return sorted_arr

for TestCase in range(int(input())):
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    indegree = [0 for _ in range(N)]
    for _ in range(K):
        a,b = map(lambda x : int(x)-1, input().split())
        graph[a].append(b)
        indegree[b] += 1
    W = int(input())
    dis = [0 for _ in range(N)]
    for i in range(N):
        if indegree[i] == 0:
            dis[i] = cost[i]
    sorted_arr = topological_sort()
    for curr in sorted_arr:
        for next in graph[curr]:
            if dis[next] < dis[curr] + cost[next]:
                dis[next] = dis[curr] + cost[next]
    print(dis[W-1])