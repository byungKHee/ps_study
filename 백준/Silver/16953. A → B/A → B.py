import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
answer = 0
Q = deque()
Q.append([A,0])
while Q:
    curr,count = Q.popleft()
    if curr*2 == B or curr*10+1 == B:
        answer = count+1
        break
    if curr*2 < B:
        Q.append([curr*2, count+1])
    if curr*10+1 < B:
        Q.append([curr*10+1, count+1])
if answer:
    print(answer+1)
else:
    print(-1)