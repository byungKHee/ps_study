from collections import defaultdict
def solution(s):
    def isPossible(target):
        d = defaultdict(int)
        for c in target:
            d[c] += 1
        if d['('] != d[')']:
            return False
        if d['{'] != d['}']:
            return False
        if d['['] != d[']']:
            return False
        return True 
    def isValid(target):
        stack = []
        for c in target:
            if not stack:   
                stack.append(c)
            else:
                if stack[-1] == '(' and c == ')':
                    stack.pop()
                elif stack[-1] == '{' and c == '}':
                    stack.pop()
                elif stack[-1] == '[' and c == ']':
                    stack.pop()
                else:
                    stack.append(c)
        if stack: return False
        return True
    
    answer = 0
    if not isPossible(s):
        return answer
    
    for target in [s[idx:] + s[:idx] for idx in range(len(s))]:
        if isValid(target):
            answer += 1    
    return answer