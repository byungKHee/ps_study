import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def func(depth, prev, start):
    if dp[start][depth][prev]:
        return dp[start][depth][prev]
    if depth == N-1:
        dp[start][depth][prev] = min([cost[depth][i] for i in range(3) if i != prev and i != start])    
        return dp[start][depth][prev]
    dp[start][depth][prev] = min([func(depth+1, i, start)+cost[depth][i] for i in range(3) if i != prev])
    return dp[start][depth][prev]

N = int(input())
dp = [[[0 for i in range(3)] for _ in range(N)] for _ in range(3)]
cost = []
for i in range(N):
    cost.append(list(map(int, input().split())))
print(min(func(1,0,0)+cost[0][0], func(1,1,1)+cost[0][1], func(1,2,2)+cost[0][2]))