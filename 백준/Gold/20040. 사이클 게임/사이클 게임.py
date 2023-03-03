import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    root = find(parent[x])
    parent[x] = root
    return root

def union(x,y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return False
    parent[x_root] = y_root
    return True

N, M = map(int, input().split())
parent = [i for i in range(N)]
answer = 0
for i in range(M):
    a,b = map(int, input().split())
    if not union(a,b):
        answer = i+1
        break
print(answer)