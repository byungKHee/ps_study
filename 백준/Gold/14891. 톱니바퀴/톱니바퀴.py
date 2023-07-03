import sys
from collections import deque
input = sys.stdin.readline

def rotate(target, direction):
    if direction == 1:
        arr[target].appendleft(arr[target].pop())
    else:
        arr[target].append(arr[target].popleft())

def dfs(target, direction):
    visited[target] = True
    left = arr[target][-2]
    right = arr[target][2]
    rotate(target, direction)
    # left
    if (0 < target) and (not visited[target-1]) and (left != arr[target-1][2]):
        dfs(target-1, -1 * direction)
    if (target < 3) and (not visited[target+1]) and (right != arr[target+1][-2]):
        dfs(target+1, -1 * direction)

arr = []
for _ in range(4):
    arr.append(deque(list(map(int, list(input().rstrip())))))

for _ in range(int(input())):
    a,b = map(int, input().split())
    visited = [False] * 4
    dfs(a-1, b)

print(arr[0][0] + 2*arr[1][0] + 4*arr[2][0] + 8*arr[3][0])