from itertools import combinations
from collections import defaultdict, Counter
def solution(orders, course):
    answer = []
    for n in course:
        count = Counter()
        for order in orders:
            if len(order) < n: continue
            count.update(list(combinations(sorted(order), n)))
        if not count: continue
        most = count.most_common(1)[0][1]
        if most < 2: continue
        for k, v in count.items():
            if v == most:
                answer.append("".join(k))

    answer.sort()
    return answer