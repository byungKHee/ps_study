import itertools
import bisect

def solution(info, query):
    
    d = {
        'java' : 1,
        'python' : 2,
        'cpp' : 3,
        'backend' : 1,
        'frontend' : 2,
        'junior' : 1,
        'senior' : 2,
        'pizza' : 1,
        'chicken' : 2
    }
    
    temp = [a.strip() for a in info]
    people = {}
    for a in temp:
        curr = ""
        for b in a.split()[:-1]:
            curr += str(d[b])
        if curr not in people:
            people[curr] = []
        people[curr].append(int(a.split()[-1]))
    for v in people.values():
        v.sort()

    answer = []
    INFO = [['java', 'python', 'cpp'], ['backend', 'frontend'], ['junior', 'senior'], ['pizza', 'chicken']]
    for q in query:
        curr = [a.strip() for a in q.split()[:-1] if a.strip() != 'and']
        idx = 0
        target = [[] for _ in range(4)]
        score = int(q.split()[-1])
        # 파싱
        for i in range(len(curr)):
            if curr[i] == '-':
                if target[idx]: idx += 1
                for j in INFO[idx]:
                    target[idx].append(d[j])
                idx += 1
                continue
            if curr[i] not in INFO[idx]:
                idx += 1
            target[idx].append(d[curr[i]])
        cnt = 0
        for comb in itertools.product(*target):
            k = ''
            for i in comb: k += str(i)
            if k not in people: continue
            l = bisect.bisect_left(people[k], score)
            cnt += len(people[k]) - l
            
        answer.append(cnt)
    return answer