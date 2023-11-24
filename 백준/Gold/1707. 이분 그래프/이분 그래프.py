import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(curr):
    visited[curr] = True
    rnt = True
    for next in graph[curr]:
        if visited[next]:
            if flag[curr] == flag[next]:
                rnt = False
        else:
            flag[next] = not flag[curr]
            rnt = dfs(next)
        if not rnt:
            break
    return rnt

for testCase in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    flag = [False] * (V+1)
    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    answer = True
    for node in range(1, V+1):
        if not visited[node]:
            if not dfs(node):
                answer = False
        if not answer:
            break
    if answer:
        print("YES")
    else:
        print("NO")