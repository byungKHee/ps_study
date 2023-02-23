import sys
from collections import deque
input = sys.stdin.readline

for Test in range(int(input())):
 
    # enter input
    N = int(input())
    lastYear = list(map(int, input().split()))
    graph = [[False for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N-1):
        for j in range(i+1, N):
            graph[lastYear[i]][lastYear[j]] = True
    M = int(input())
    
    # graph preprocessing
    for i in range(M):
        a,b = map(int, input().split())
        temp = graph[a][b]
        graph[a][b] = graph[b][a]
        graph[b][a] = temp
    indegree = [0 for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[j+1][i+1]:
                indegree[i] += 1
    
    # topological sort
    flag = 0
    answer = []
    Q = deque()
    for i in range(N):
        if indegree[i] == 0:
            Q.append(i)
    for i in range(N):
        if not Q:
            flag = 2
            break
        if len(Q) >= 2:
            flag = 1
        curr = Q.popleft()
        answer.append(curr+1)
        for i in range(N):
            if graph[curr+1][i+1]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    Q.append(i)
    
    # print answer
    if flag == 0:
        for n in answer: print(n, end=' ')
    if flag == 1:
        print('?')
    if flag == 2:
        print('IMPOSSIBLE')