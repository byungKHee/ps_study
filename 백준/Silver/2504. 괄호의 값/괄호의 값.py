import sys
input = sys.stdin.readline

arr = input().rstrip()
stack = []
for c in arr:
    if not stack:
        stack.append(c)
    elif stack[-1] == '(' and c == ')':
        stack.pop()
    elif stack[-1] == '[' and c == ']':
        stack.pop()
    else:
        stack.append(c)
if stack:
    print(0)
else:
    for c in arr:
        if not stack:
            stack.append(c)
            continue
        if c == ')':
            value = 0
            top = stack.pop()
            while top != '(':
                value += top
                top = stack.pop()
            if value:
                stack.append(value*2)
            else:
                stack.append(2)
        elif c == ']':
            value = 0
            top = stack.pop()
            while top != '[':
                value += top
                top = stack.pop()
            if value:
                stack.append(value*3)
            else:
                stack.append(3)
        else:
            stack.append(c)
    print(sum(stack))