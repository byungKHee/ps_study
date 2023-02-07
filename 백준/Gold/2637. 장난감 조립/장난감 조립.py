import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    x,y,k = map(int, input().split())
    graph[x].append((y,k))
    indegree[y] += 1

Q = deque()
answer = [0 for i in range(N+1)]
base = []
for i in range(1, N+1):
    if indegree[i] == 0:
        Q.append(i)
        answer[i] = 1

for _ in range(N):
    curr = Q.popleft()
    if not graph[curr]:
        base.append(curr)
    for next, cost in graph[curr]:
        answer[next] += answer[curr] * cost
        indegree[next] -= 1
        if indegree[next] == 0:
            Q.append(next)
            
base.sort()
for n in base:
    print(f"{n} {answer[n]}")
