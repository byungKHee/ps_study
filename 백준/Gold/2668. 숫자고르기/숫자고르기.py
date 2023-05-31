import sys
input = sys.stdin.readline

def dfs(curr, visited):
    visited.append(curr)
    next = arr[curr]
    if next in visited:
        if next in answer:
            return
        else:
            answer.append(next)
            dfs(next, visited.copy())
    dfs(next, visited.copy())
        
N = int(input())
arr = [int(input()) - 1 for _ in range(N)]
answer = []
for start in range(N):
    if start not in answer:
        dfs(start, [])
print(len(answer))
answer.sort()
for n in answer:
    print(n+1)