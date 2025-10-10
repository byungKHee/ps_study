from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for arr in permutations(dungeons, len(dungeons)):
        cnt = 0
        health = k
        for require, cost in arr:
            if require <= health:
                cnt += 1
                health -= cost
            else:
                break
        answer = max(answer, cnt)
    
    return answer