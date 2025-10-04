from collections import defaultdict
from math import ceil
def f(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def solution(fees, records):
    timer = defaultdict(int)
    park = {}
    for record in records:
        status = record.split()
        if status[2] == 'IN':
            park[status[1]] = f(status[0])
        else:
            out_time = f(status[0])
            in_time = park[status[1]]
            timer[status[1]] += out_time - in_time
            del park[status[1]]
    for k, v in park.items():
        timer[k] += f("23:59") - v
    
    rnt = []
    for k, v in timer.items():
        fee = fees[1] + max(0, ceil((v - fees[0]) / fees[2])) * fees[3]
        rnt.append([int(k), fee])
    rnt.sort(key=lambda x : x [0])
    answer = [a[1] for a in rnt]
    return answer