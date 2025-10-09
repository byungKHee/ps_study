from bisect import bisect_left, bisect_right


# 실패율 = (n > target >= n) / (target >= n)
def solution(N, stages):
    answer = []
    stages.sort()
    failures = []
    prev = 0
    for n in range(1, N+1):    
        l = bisect_left(stages, n)
        r = bisect_right(stages, n)
        
        top = r - l
        bottom = len(stages) - l
        fail = 0
        if bottom:
            fail = top / bottom
    
        failures.append([n, fail])
        
    failures.sort(key=lambda x : x[1], reverse=True)
    answer = [a[0] for a in failures]
    
    return answer