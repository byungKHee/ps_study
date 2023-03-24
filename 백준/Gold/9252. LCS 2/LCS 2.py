import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
if not dp[-1][-1]:
    print(0)
    sys.exit()
answer = []
x = len(A)
y = len(B)
while x and y:
    if dp[x-1][y] == dp[x][y]:
        x -= 1
        continue
    if dp[x][y-1] == dp[x][y]:
        y -= 1
        continue
    answer.append(A[x-1])
    x -= 1
    y -= 1
print(dp[-1][-1])
for i in answer[::-1]:
    print(i,end='')