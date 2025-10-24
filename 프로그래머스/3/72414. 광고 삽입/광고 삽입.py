def func(t):
    s = list(map(int, t.split(':')))
    return s[0] * 3600 + s[1] * 60 + s[2]

def make_answer(n):
    a = n // 3600
    n %= 3600
    b = n // 60
    n %= 60
    c = n
    rnt = ''
    if a < 10:
        rnt += '0' + str(a)
    else:
        rnt += str(a)
    rnt += ':'
    if b < 10:
        rnt += '0' + str(b)
    else:
        rnt += str(b)
    rnt += ':'
    if c < 10:
        rnt += '0' + str(c)
    else:
        rnt += str(c)
    return rnt
        
    
def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    arr = [0] * (func(play_time) + 2)
    L = func(adv_time)
    for log in logs:
        s, e = map(func, log.split('-'))
        arr[s] += 1
        arr[e] -= 1
    curr = arr[0]
    # 누적합
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
        if i < L:
            curr += arr[i]

    total = curr
    answer = 0
    for i in range(L, len(arr)-1):
        curr += arr[i]
        curr -= arr[i-L]
        if total < curr:
            total = curr
            answer = i-L+1
    
    # print(answer)
    return make_answer(answer)
    