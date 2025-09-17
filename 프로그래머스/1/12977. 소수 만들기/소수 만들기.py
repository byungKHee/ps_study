from itertools import combinations
def solution(nums):
    answer = 0
    isPrime = [True] * 4000
    
    for i in range(2, 200):
        if isPrime[i]:
            for j in range(i*i, 4000, i):
                isPrime[j] = False
    
    for arr in combinations(nums, 3):
        if isPrime[sum(arr)]:
            answer += 1

    return answer