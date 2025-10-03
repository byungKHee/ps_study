group = [[0] * 50 for _ in range(50)]
value = {}
ID = 2500

def update(command):
    global group, value, ID
    order = command.split()
    if len(order) == 3:
        r, c = int(order[0]) - 1, int(order[1]) - 1
        g = group[r][c]
        value[g] = order[2]
    else:
        for i in range(50):
            for j in range(50):
                if value[group[i][j]] == order[0]:
                    value[group[i][j]] = order[1]

def merge(command):
    global group, value, ID
    r1,c1,r2,c2 = map(lambda x : int(x)-1, command.split())
    if r1 == r2 and c1 == c2: return
    g1 = group[r1][c1]
    g2 = group[r2][c2]
    
    # 둘 다 merge 안됨 -> 새로운 group_id 발급 후 값 할당
    if g1 == r1 * 50 + c1 and g2 == r2 * 50 + c2:
        new_value = ''
        if value[g1] != '':
            new_value = value[g1]
        else:
            new_value = value[g2]
        group[r1][c1] = ID
        group[r2][c2] = ID
        value[ID] = new_value
        ID += 1
    # 둘 다 merge
    elif g1 != r1 * 50 + c1 and g2 != r2 * 50 + c2:
        new_value = ''
        if value[g1] != '':
            new_value = value[g1]
        else:
            new_value = value[g2]
        for i in range(50):
            for j in range(50):
                if group[i][j] == g1:
                    group[i][j] = g2
        value[g2] = new_value
    # g1만 merge
    elif g1 != r1 * 50 + c1:
        new_value = ''
        if value[g1] != '':
            new_value = value[g1]
        else:
            new_value = value[g2]
        group[r2][c2] = g1
        value[g1] = new_value
    # g2만 merge
    else:
        new_value = ''
        if value[g1] != '':
            new_value = value[g1]
        else:
            new_value = value[g2]
        group[r1][c1] = g2
        value[g2] = new_value

def unmerge(command):
    global group, value, ID
    r,c = map(lambda x : int(x)-1, command.split())
    # 병합된 적 없음
    g = group[r][c]
    v = value[g]
    for i in range(50):
        for j in range(50):
            if group[i][j] == g:
                group[i][j] = i * 50 + j
                value[i*50+j] = ''
    value[r*50 + c] = v

def solution(commands):
    global group, value, ID
    answer = []
    for i in range(50):
        for j in range(50):
            group[i][j] = i * 50 + j
            value[i*50 + j] = ''
    
    for command in commands:
        order = command.split()[0]
        if order == 'UPDATE':
            update(command[7:])
        elif order == 'MERGE':
            merge(command[6:])
        elif order == 'UNMERGE':
            unmerge(command[8:])
        else:
            r,c = map(int, command[6:].split())
            g = group[r-1][c-1]
            if g not in value or value[g] == '':
                answer.append('EMPTY')
            else:
                answer.append(value[g])
        # for i in range(10):
        #     for j in range(10):
        #         print(group[i][j], end=' ')
        #     print()
        # for i in range(10):
        #     for j in range(10):
        #         print(value[group[i][j]], end=' ')
        #     print()
        
    return answer