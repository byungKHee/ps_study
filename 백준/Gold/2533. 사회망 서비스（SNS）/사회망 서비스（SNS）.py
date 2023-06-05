import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(curr):
    visited[curr] = True
    dp[curr][0] = 0
    dp[curr][1] = 1
    for child in graph[curr]:
        if visited[child]:
            continue
        dfs(child)
        dp[curr][0] += dp[child][1]
        dp[curr][1] += min(dp[child][0], dp[child][1])   

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[-1,-1] for _ in range(N+1)]
visited = [False] * (N+1)
dfs(1)
print(min(dp[1][0], dp[1][1]))