def convert(n, k):
    rnt = ''
    while n >= k:
        rnt = str(n % k) + rnt
        n //= k
    rnt = str(n) + rnt
    return rnt

def solution(n, k):
    # isPrime = [True] * 10000000
    # isPrime[1] = False
    # for i in range(2, int(10000000 ** 0.5) + 1):
    #     if not isPrime[i]:
    #         continue
    #     for j in range(i*i, 10000000, i):
    #         isPrime[j] = False
    
    s = convert(n,k)
    targets = s.split('0')
    
    answer = 0
    for n in targets:
        if len(n) == 0: continue
        target = int(n.strip())
        if target < 2: continue
        if target == 2:
            answer += 1
            continue
        isPrime = True
        for i in range(2, int(target**0.5) + 1):
            if target % i == 0:
                isPrime = False
                break
        if isPrime:
            answer += 1
    return answer