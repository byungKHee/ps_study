import sys
# from queue import PriorityQueue
# from queue import Queue
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited[start] = 0
    Q = deque()
    Q.append(start)
    while Q:
        curr = Q.popleft()
        for next in tree[curr]:
            if visited[next[0]] == -1:
                visited[next[0]] = visited[curr] + next[1]
                Q.append(next[0])

    return max(visited)

V = int(input())
tree = [[] for _ in range(V)]
for i in range(V):
    s = list(map(int, input().rstrip().split()))
    for j in range(1, len(s)-1, 2):
        tree[s[0]-1].append((s[j]-1, s[j+1]))
    
visited = [-1 for _ in range(V)]
dis = bfs(0)
idx = visited.index(dis)
visited = [-1 for _ in range(V)]
print(bfs(idx))