import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
cost = [0 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for i in range(1, N+1):
    arr = list(map(int, input().split()))
    cost[i] = arr[0]
    for j in range(1, len(arr)-1):
        graph[arr[j]].append(i)
        indegree[i] += 1

answer = cost[:]
order = []
Q = deque()
for i in range(1, N+1):
    if indegree[i] == 0: Q.append(i)
for _ in range(N):
    curr = Q.popleft()
    order.append(curr)
    for next in graph[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            Q.append(next)

for curr in order:
    for next in graph[curr]:
        answer[next] = max(answer[next], answer[curr] + cost[next])
        
for i in range(1,N+1): print(answer[i])