import sys
from collections import deque
input = sys.stdin.readline

def move(direction, arr):
    global answer
    rnt = [[0 for _ in range(N)] for _ in range(N)]
    if direction == 0:  # up
        for i in range(N):
            queue = deque()
            result = deque()
            for j in range(N):
                curr = arr[j][i]
                if curr == 0:
                    continue
                if not queue:
                    queue.appendleft(curr)
                elif queue[0] == curr:
                    queue[0] *= 2
                    answer = max(answer, curr*2)
                    while queue:
                        result.appendleft(queue.pop())
                else:
                    queue.appendleft(curr)
            while queue:
                result.appendleft(queue.pop())
            for j in range(N):
                if not result:
                    break
                rnt[j][i] = result.pop()
    
    if direction == 1:  # down
        for i in range(N):
            queue = deque()
            result = deque()
            for j in range(N):
                curr = arr[N-j-1][i]
                if curr == 0:
                    continue
                if not queue:
                    queue.appendleft(curr)
                elif queue[0] == curr:
                    queue[0] *= 2
                    answer = max(answer, curr*2)
                    while queue:
                        result.appendleft(queue.pop())
                else:
                    queue.appendleft(curr)
            while queue:
                result.appendleft(queue.pop())
            for j in range(N):
                if not result:
                    break
                rnt[N-j-1][i] = result.pop()    
    
    if direction == 2:  # right
        for i in range(N):
            queue = deque()
            result = deque()
            for j in range(N):
                curr = arr[i][N-j-1]
                if curr == 0:
                    continue
                if not queue:
                    queue.appendleft(curr)
                elif queue[0] == curr:
                    queue[0] *= 2
                    answer = max(answer, curr*2)
                    while queue:
                        result.appendleft(queue.pop())
                else:
                    queue.appendleft(curr)
            while queue:
                result.appendleft(queue.pop())
            for j in range(N):
                if not result:
                    break
                rnt[i][N-j-1] = result.pop()    
    
    if direction == 3:  # left
        for i in range(N):
            queue = deque()
            result = deque()
            for j in range(N):
                curr = arr[i][j]
                if curr == 0:
                    continue
                if not queue:
                    queue.appendleft(curr)
                elif queue[0] == curr:
                    queue[0] *= 2
                    answer = max(answer, curr*2)
                    while queue:
                        result.appendleft(queue.pop())
                else:
                    queue.appendleft(curr)
            while queue:
                result.appendleft(queue.pop())
            for j in range(N):
                if not result:
                    break
                rnt[i][j] = result.pop()
    return rnt

N = int(input())
start = []
for _ in range(N):
    start.append(list(map(int, input().split())))
answer = 0
for i in start:
    answer = max(answer, max(i))
Q = deque()
Q.append([0, start])
while Q:
    count, curr = Q.popleft()
    if count == 5:
        break
    for i in range(4):
        if count == 4:
            move(i,curr)
        else:
            Q.append([count+1, move(i,curr)])
print(answer)