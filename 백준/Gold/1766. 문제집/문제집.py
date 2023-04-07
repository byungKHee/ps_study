import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
Q = []
answer = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(Q, i)
for _ in range(N):
    curr = heapq.heappop(Q)
    answer.append(curr)
    for next in graph[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(Q, next)
print(*answer)