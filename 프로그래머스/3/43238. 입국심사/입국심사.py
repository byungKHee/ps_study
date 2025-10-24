def check(limit, target, times):
    total = 0
    for n in times:
        total += limit // n
    
    # 가능
    if total >= target:
        return True
    # 불가능
    return False
        
def solution(n, times):
    answer = 0
    
    lo = -1
    hi = 100000000000000
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid, n, times):
            hi = mid
        else:
            lo = mid
            
    return hi