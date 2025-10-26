def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    for i, n in enumerate(A):
        answer += n * B[i]
    return answer