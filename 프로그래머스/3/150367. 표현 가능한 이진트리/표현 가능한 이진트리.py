def make_tree(num):
    diff = 1
    rnt = []
    while diff <= num:
        if diff & num:
            rnt.append(True)
        else:
            rnt.append(False)
        diff *= 2
    if len(rnt) % 2 == 0:
        rnt.append(False)
    size = len(rnt)
    i = 0
    while 2 ** i - 1 < size:
        i += 1
    for j in range(2**i - 1 - size):
        rnt.append(False)
    rnt.reverse()
    return rnt

def possible(tree):
    if len(tree) == 1:
        return True
    root = len(tree) // 2
    if not tree[root] and any(tree):
        return False
    return possible(tree[0:root]) and possible(tree[root+1:])
    
def solve(target):
    tree = make_tree(target)
    if possible(tree):
        return True
    return False

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(int(solve(n)))
    return answer