visited = {}
def isValid(s):
    if s in visited:
        return visited[s]
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
            continue
        if ch == '(':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)

    visited[s] = (len(stack) == 0)
    return visited[s]
            
def func(s):
    if not s: return s
    l = 0
    r = 0
    u = ''
    v = ''
    for i, c in enumerate(s):
        if c == '(':
            l += 1
        else:
            r += 1
        if l == r:
            u = s[:i+1]
            if i + 1 != len(s):
                v = s[i+1:]
            break
    print(f"u: {u}, v: {v}")
    if isValid(u):
        return u + func(v)
    else:
        rnt = '(' + func(v) + ')'
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                rnt += ')'
            else:
                rnt += '('
        return rnt


def solution(p):
    if isValid(p):
        return p
    try:
        return func(p)
    except:
        return 'test'