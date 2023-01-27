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
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[x_root] = y_root
        return True
    return False

def dis(a,b):
    return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))

N = int(input())
graph = []
planet = []
for i in range(N):
    x,y,z = map(int, input().split())
    planet.append((x,y,z,i))

for i in range(3):
    planet.sort(key=lambda x : x[i])
    for j in range(N-1):
        graph.append((abs(planet[j][i] - planet[j+1][i]), planet[j][3], planet[j+1][3]))

graph.sort(key=lambda x: x[0])
parent = [i for i in range(N)]
count = 0
answer = 0
for w,a,b in graph:
    if union(a,b):
        count += 1
        answer += w
    if count == N-1:
        break
print(answer)