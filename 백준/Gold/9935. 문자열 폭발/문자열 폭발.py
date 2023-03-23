import sys
from collections import deque
input = sys.stdin.readline

arr = input().rstrip()
bomb = list(input().rstrip())
bombSize = len(bomb)
stack = []
for c in arr:
    stack.append(c)
    if stack[-1] == bomb[-1] and len(stack) >= bombSize:
        if stack[-bombSize:] == bomb:
            for _ in range(bombSize):
                stack.pop()
if stack:
    for c in stack:
        print(c, end='')
else:
    print('FRULA')