# 정규식 없이 도전~
def solution(new_id):
    answer = ''    
    # 1단계
    new_id = new_id.lower()
    # 2단계
    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    new_id = "".join(ch for ch in new_id if ch in allowed)
    # 3단계
    rnt = ""
    prev_dot = False
    for s in new_id:
        if prev_dot:
            if s == '.':
                continue
            else:
                prev_dot = False
                rnt += s
        else:
            if s == '.':
                prev_dot = True
                rnt += s
            else:
                rnt += s
    new_id = rnt
    
    # 4단계
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 5단계
    if not new_id:
        new_id = "a"
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id += new_id[-1]
    
    return new_id