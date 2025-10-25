
def solution(N, number):
    dp = [set() for _ in range(8)]
    
    # N 한 번으로 만들 수 있는거
    for i in range(1, 9):
        dp[i-1].add(int(str(N) * i))
    if number in dp[0]:
        return 1
    
    for target in range(1, 8):
        for j in range(target):
            for a in dp[j]:
                for b in dp[target-j - 1]:
                    dp[target].add(a + b)
                    if a >= b:
                        dp[target].add(a - b)
                    dp[target].add(a * b)
                    if b != 0 and a // b != 0:
                        dp[target].add(a // b)
        if number in dp[target]:
            return target + 1

    return -1