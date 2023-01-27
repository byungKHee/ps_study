import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        root = find(parent[x])
        parent[x] = root
        return root

def union(x,y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[x_root] = y_root
        return True
    return False

N = int(input())
M = int(input())
parent = [x for x in range(N+1)]
graph = []
for _ in range(M):
    a,b,w = map(int, input().split())
    graph.append((w,a,b))
graph.sort(key=lambda x : x[0])
count = 0
answer = 0
for (w,a,b) in graph:
    if union(a,b):
        count += 1
        answer += w
    if count == N-1:
        break
print(answer)