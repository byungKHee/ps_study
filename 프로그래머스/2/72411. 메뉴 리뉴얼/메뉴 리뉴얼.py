from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for n in course:
        count = defaultdict(int)
        for order in orders:
            if len(order) < n: continue
            for comb in list(combinations(order, n)):
                comb = sorted(list(comb))
                curr = "".join(comb)
                count[curr] += 1
        M = 0
        arr = []
        for k,v in count.items():
            if v < 2: continue
            if M == v:
                arr.append(k)
            elif M < v:
                arr.clear()
                arr.append(k)
                M = v
        answer.extend(arr)

    answer.sort()
    return answer