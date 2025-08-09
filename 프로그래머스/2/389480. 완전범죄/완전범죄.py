def solution(info, n, m):
    global answer

    answer = float('inf')
    
    visited = set()
    
    def func(idx, n_left, m_left):
        global answer
        if (idx, n_left, m_left) in visited:
            return
        else:
            visited.add((idx, n_left, m_left))
        if idx == len(info):
            answer = min(answer, n - n_left)
            return
        if info[idx][1] < m_left:
            func(idx+1, n_left, m_left - info[idx][1])
        if info[idx][0] < n_left:
            func(idx+1, n_left - info[idx][0], m_left)
    
    func(0, n, m)
    if answer == float('inf'):
        return -1
    return answer