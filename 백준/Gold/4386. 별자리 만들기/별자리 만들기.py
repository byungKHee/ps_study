import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    root = find(parent[x])
    parent[x] = root
    return root

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return False
    parent[root_x] = root_y
    return True

def dis(a,b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return (dx**2 + dy**2)**(0.5)

N = int(input())
arr = []
edges = []
parent = [i for i in range(N)]
for _ in range(N):
    arr.append(list(map(float, input().split())))
for i in range(N-1):
    for j in range(i+1, N):
        edges.append([dis(arr[i], arr[j]), i, j])

edges.sort()
answer = 0
count = 0
for w,a,b in edges:
    if union(a,b):
        answer += w
        count += 1
        if count == N:
            break
print(answer)