def solution(gems):
    answer = []
    
    total = 0
    f = dict()
    for s in set(gems):
        if s not in f:
            f[s] = total
        total += 1
    l = r = 0
    curr = [0] * total
    answer = [0,0]
    min_cnt = len(gems) + 2
    while r <= len(gems) and l <= r:
        if all(curr):
            if r - l + 1 < min_cnt:
                min_cnt = r - l + 1
                answer = [l+1, r]
            curr[f[gems[l]]] -= 1
            l += 1
        else:
            if r == len(gems):
                break
            curr[f[gems[r]]] += 1
            r += 1
        
    return answer