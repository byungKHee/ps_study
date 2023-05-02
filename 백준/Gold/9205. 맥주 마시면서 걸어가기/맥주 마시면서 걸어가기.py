import sys
input = sys.stdin.readline

def dis(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def dfs(curr):
    visited[curr] = True
    for next in graph[curr]:
        if not visited[next]:
            dfs(next)

for testCase in range(int(input())):
    N = int(input())
    arr = []
    for _ in range(N+2):
        arr.append(list(map(int, input().split())))
    graph = [[] for _ in range(N+2)]
    for i in range(N+1):
        for j in range(i+1, N+2):
            if dis(arr[i], arr[j]) <= 1000:
                graph[i].append(j)
                graph[j].append(i)
    visited = [False] * (N+2)
    dfs(0)
    if visited[N+1]:
        print('happy')
    else:
        print('sad')