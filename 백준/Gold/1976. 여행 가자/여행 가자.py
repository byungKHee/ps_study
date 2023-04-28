import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
goal = list(map(lambda x : int(x)-1, input().split()))
for i in range(N):
    graph[i][i] = True
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                continue
            else:
                graph[i][j] = graph[i][k] and graph[k][j]
answer = True
for i in range(M-1):
    if not graph[goal[i]][goal[i+1]]:
        answer = False
        break
if answer:
    print("YES")
else:
    print('NO')