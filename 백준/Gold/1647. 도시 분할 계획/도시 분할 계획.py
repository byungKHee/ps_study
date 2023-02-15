import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
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

V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
for _ in range(E):
    a,b,w = map(int, input().split())
    edges.append((w,a,b))
edges.sort()

count = 0
answer = 0
max_road = 0
for w,a,b in edges:
    if union(a,b):
        count += 1
        answer += w
        max_road = max(max_road, w)
    if count == V-1:
        break
print(answer-max_road)