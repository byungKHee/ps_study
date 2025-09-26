def batch(s, n):
    l = len(s)
    rnt = []
    for i in range(0, l, n):
        rnt.append(s[i : min(l, i + n)])
    return rnt

def solution(s):
    answer = len(s)
    for slice in range(1, len(s)//2 + 1):
        curr = 0
        cnt = 1
        arr = batch(s, slice)
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                cnt += 1
            else:
                if cnt == 1:
                    curr += slice
                else:
                    curr += slice + len(str(cnt))
                cnt = 1
        if cnt == 1:
            curr += len(arr[-1])
        else:
            curr += slice + len(str(cnt))
        answer = min(answer, curr)

    return answer