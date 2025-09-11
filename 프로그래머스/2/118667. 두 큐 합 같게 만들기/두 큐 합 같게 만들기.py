from bisect import bisect_left, bisect_right
    

def solution(queue1, queue2):
    arr = []
    for n in queue1: arr.append(n)
    for n in queue2: arr.append(n)
    dp = [0]
    for n in arr: dp.append(dp[-1] + n)
    
    if dp[-1] % 2 == 1:
        return -1
    if sum(queue1) == sum(queue2):
        return 0
    size = len(queue1)
    def func(l,r):
        cnt = l
        mid = size - 1
        if mid < r:
            cnt += r - mid            
        elif mid > r:
            cnt += size + r
        return cnt
    answer = 150000000
    for i in range(len(dp)-1):
        target = dp[-1] // 2 + dp[i]
        left = bisect_left(dp, target, i+1)
        right = bisect_right(dp, target, i+1)
        if left != right:
            answer = min(answer, func(i, left-1))
            continue
    if answer == 150000000:
        return -1
    return answer