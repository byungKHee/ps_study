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
    a = find(x)
    b = find(y)
    if a == b:
        return False
    else:
        parent[a] = b
        return True

n,m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    t,a,b = map(int, input().split())
    if t == 0:
        union(a,b)
    else:
        A = find(a)
        B = find(b)
        if A == B:
            print("YES")
        else:
            print("NO")