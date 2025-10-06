def solution(alp, cop, problems):

    max_alp = max([a[0] for a in problems])
    max_cop = max([a[1] for a in problems])
    
    if max_alp <= alp and max_cop <= cop:
        return 0
    
    if max_alp < alp:
        max_alp = alp
    if max_cop < cop:
        max_cop = cop
    
    dp = [[100000000] * (max_cop + 1) for _ in range(max_alp + 1)]

    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for p in problems:
                if i < p[0] or j < p[1]: continue
                
                x = min(i+p[2], max_alp)
                y = min(j+p[3], max_cop)
                
                dp[x][y] = min(dp[x][y], dp[i][j] + p[4])
    
    
    return dp[max_alp][max_cop]