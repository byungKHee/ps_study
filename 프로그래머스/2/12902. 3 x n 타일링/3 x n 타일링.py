MOD = 1_000_000_007
def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(2, n+1):
        if i >= 2:
            dp[i] = (dp[i] + dp[i-2] * 3) % MOD
        for prev in range(4, n+1, 2):
            if i - prev < 0: break
            dp[i] = (dp[i] + dp[i - prev] * 2) % MOD
    return dp[n] % MOD