def solution(n, w, num):
    answer = 0
    target = 0
    for i in range(num, n+1):
        x = (i-1) // w
        y = (i-1) % w
        if x % 2 == 1:
            y = w - y - 1
        if i == num:
            target = y
        if y == target:
            answer += 1
    return answer