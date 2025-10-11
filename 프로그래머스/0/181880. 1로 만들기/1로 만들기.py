def func(n):
    cnt = 0
    while n != 1:
        n //= 2
        cnt += 1
    return cnt

def solution(num_list):
    answer = 0
    for n in num_list:
        answer += func(n)
    return answer