def solution(record):
    answer = []
    name = {}
    display = []
    # 최종 닉네임 설정
    for r in record:
        s = r.split()
        if len(s) == 2:
            display.append(['out', s[1]])
        elif s[0] == 'Enter':
            name[s[1]] = s[2]
            display.append(['in', s[1]])
        else:
            name[s[1]] = s[2]
    for d in display:
        if d[0] == 'in':
            answer.append(f"{name[d[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{name[d[1]]}님이 나갔습니다.")
    
    return answer