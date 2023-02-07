import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]):
        graph[arr[i]].append(arr[i+1])
        indegree[arr[i+1]] += 1
        
Q = deque()
cycle = False
answer = []
for i in range(1, N+1):
    if indegree[i] == 0:
        Q.append(i)

for _ in range(N):
    if not Q:
        cycle = True
        break
    curr = Q.popleft()
    answer.append(curr)
    for next in graph[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            Q.append(next)
            
if cycle:
    print(0)
else:
    for n in answer: print(n)