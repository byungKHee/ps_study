def find_last(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i]:
            return i
    return -1

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_last = find_last(deliveries)
    p_last = find_last(pickups)
    while True:
        if d_last == -1 and p_last == -1:
            break
        answer += (max(d_last, p_last) + 1) * 2
        
        # 배달물 전달
        cnt = cap
        for i in range(d_last, -1, -1):
            if not deliveries[i]:
                d_last -= 1
                continue
            if cnt <= deliveries[i]:
                deliveries[i] -= cnt
                d_last = i
                if deliveries[i] == 0:
                    while d_last >= 0 and deliveries[d_last] == 0:
                        d_last -= 1
                break
            else:
                cnt -= deliveries[i]
                deliveries[i] = 0
                d_last -= 1
        cnt = cap
        # 수거
        for i in range(p_last, -1, -1):
            if not pickups[i]:
                p_last -= 1
                continue
            if cnt <= pickups[i]:
                pickups[i] -= cnt
                p_last = i
                if pickups[i] == 0:
                    while p_last >= 0 and pickups[p_last] == 0:
                        p_last -= 1
                break
            else:
                cnt -= pickups[i]
                pickups[i] = 0
                p_last -= 1
    return answer