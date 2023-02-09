import sys
from collections import deque
input = sys.stdin.readline

def func(start):
    Q = deque([start])
    while Q:
        curr = Q.popleft()
        if curr % 3 == 0 and not visited[curr//3]:
            Q.append(curr//3)
            visited[curr//3] = curr
        if curr % 2 == 0 and not visited[curr//2]:
            Q.append(curr//2)
            visited[curr//2] = curr
        if not visited[curr-1]:
            Q.append(curr-1)
            visited[curr-1] = curr        
        if visited[1]:
            break

N = int(input())
visited = [0 for _ in range(N+1)]
visited[N] = N
func(N)
answer = []
count = 0
idx = 1
while visited[idx] != idx:
    answer.append(idx)
    idx = visited[idx]
    count += 1
answer.append(N)
print(count)
for i in answer[::-1]:
    print(i, end=' ')