from itertools import combinations

# def inter(a,b):
#     i = 0
#     j = 0
#     rnt = 0
#     while i < 5 and j < 5:
#         if a[i] == b[j]:
#             rnt += 1
#             i += 1
#             j += 1
#         elif a[i] < b[j]:
#             i += 1
#         else:
#             j += 1
#     return rnt

def solution(n, q, ans):
    answer = 0
    
    for curr in combinations(range(1, n+1), 5):
        impossible = False
        for i in range(len(q)):
            if len(set(q[i]) & set(curr)) != ans[i]:
                impossible = True
                break
        if impossible:
            continue
        answer += 1
    
    
    return answer