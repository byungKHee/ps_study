def solution(s):
    answer = len(s)
    for slice in range(1, len(s)//2 + 1):
        idx = 0
        prev = s[idx : idx + slice]
        cnt = 0
        curr = ""
        while idx + slice <= len(s):
            # 앞과 같다면
            if prev == s[idx: idx + slice]:
                cnt += 1
            else:
                if cnt == 1:
                    curr += prev
                    prev = s[idx: idx + slice]
                    cnt = 1
                else:
                    curr += str(cnt) + prev
                    prev = s[idx: idx + slice]
                    cnt = 1
            idx += slice
        # 마지막 처리
        if cnt != 0:
            if cnt == 1:
                curr += prev
            else:
                curr += str(cnt) + prev
        # 남은 짜투리 처리
        if len(s) % slice:
            curr += s[-1 * (len(s) % slice): ]
        answer = min(answer, len(curr))
    return answer