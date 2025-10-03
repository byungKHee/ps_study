from itertools import combinations, product
from bisect import bisect_left
def solution(dice):
    answer = []
    max_win = 0
    for comb in list(combinations([i for i in range(len(dice))], len(dice) // 2)):
        A = [dice[i] for i in comb]
        B = [dice[i] for i in range(len(dice)) if i not in comb]
        A_sum = []
        B_sum = []
        for a in product(*A):
            A_sum.append(sum(a))
        for b in product(*B):
            B_sum.append(sum(b))
        A_sum.sort()
        B_sum.sort()
        win = 0
        for n in A_sum:
            idx = bisect_left(B_sum, n)
            win += idx # 이기거나 비긴 횟수
        if win >= max_win:
            max_win = win
            answer = list(comb)
    for i in range(len(answer)):
        answer[i] += 1
    answer.sort()
    return answer