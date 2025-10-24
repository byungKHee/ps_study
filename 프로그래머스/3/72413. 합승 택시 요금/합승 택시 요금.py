def solution(n, s, a, b, fares):
    IMPOSSIBLE = 1000000000
    dis = [[IMPOSSIBLE] * n for _ in range(n)]
    for i in range(n):
        dis[i][i] = 0
    for i,j,w in fares:
        i -= 1
        j -= 1
        dis[i][j] = w
        dis[j][i] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    
    answer = dis[s-1][a-1] + dis[s-1][b-1]

    for mid in range(n):
        answer = min(answer, dis[s-1][mid] + dis[mid][a-1] + dis[mid][b-1])
    return answer