from collections import deque


def solution(queue1, queue2):
    answer = 0
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    q_sum1 = sum(queue1)
    q_sum2 = sum(queue2)
    size = len(queue1)
    
    while answer < 4*size:      
        if q_sum1 > q_sum2:
            n = q1.popleft()
            q2.append(n)
            q_sum1 -= n
            q_sum2 += n
        elif q_sum1 < q_sum2:
            n = q2.popleft()
            q1.append(n)
            q_sum1 += n
            q_sum2 -= n
        else:
            return answer
        answer += 1
    return -1