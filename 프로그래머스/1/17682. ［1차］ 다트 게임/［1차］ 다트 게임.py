import re
pattern = re.compile(r'(\d+)([SDT])([*#]?)')

def single(arr):
    n = int(arr[0])
    if arr[1] == 'S':
        return n
    if arr[1] == 'D':
        return n ** 2
    if arr[1] == 'T':
        return n ** 3

def solution(dartResult):
    answer = 0
    arr = re.findall(pattern, dartResult)
    stack = []
    for step, curr in enumerate(arr):
        if curr[2] == '*':
            if stack: stack[-1] *= 2
            stack.append(2 * single(curr))
        elif curr[2] == '#':
            stack.append(-1 * single(curr))
        else:
            stack.append(single(curr))

    return sum(stack)
