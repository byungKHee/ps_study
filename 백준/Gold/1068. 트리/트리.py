import sys
input = sys.stdin.readline

def update(curr):
    valid[curr] = False
    for next in child[curr]:
        update(next)

N = int(input())
parent = list(map(int, input().split()))
child = [[] for _ in range(N)]
for node in range(N):
    if parent[node] != -1:
        child[parent[node]].append(node)
valid = [True for _ in range(N)]
target = int(input())
if parent[target] != -1:
    child[parent[target]].remove(target)
update(target)
answer = 0
for node in range(N):
    if not child[node] and valid[node]:
        answer += 1
print(answer)