def solution(board, skill):
    answer = 0
    diff = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    S = [0, -1, 1]
    for t, r1, c1, r2, c2, value in skill:
        diff[r1][c1] += S[t] * value
        diff[r1][c2+1] -= S[t] * value
        diff[r2+1][c1] -= S[t] * value
        diff[r2+1][c2+1] += S[t] * value
        
    # diff 누적합
    for i in range(len(board)):
        for j in range(len(board[0])):
            diff[i][j+1] += diff[i][j]
        
    for j in range(len(board[0])):
        for i in range(len(board)):
            diff[i+1][j] += diff[i][j]
            
    # 합산
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + diff[i][j] > 0:
                answer += 1
        
    return answer