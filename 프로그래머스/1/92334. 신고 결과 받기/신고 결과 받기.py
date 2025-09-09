def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    d = {}
    cnt = {}
    for id in id_list:
        d[id] = set()
        cnt[id] = 0
    for s in report:
        a,b = s.split()
        d[a].add(b)
    for id in id_list:
        for target in list(d[id]):
            cnt[target] += 1
    for i, id in enumerate(id_list):
        for target in list(d[id]):
            if cnt[target] >= k:
                answer[i] += 1
    return answer