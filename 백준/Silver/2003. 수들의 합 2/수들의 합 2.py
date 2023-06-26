import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
for i in range(1, N):
    S[i] += S[i-1]
S.insert(0,0)
l,r = 0,1
answer = 0
while True:
    if r > N:
        break
    curr = S[r] - S[l]
    if curr < M:
        r += 1
    elif curr > M:
        l += 1
    else:
        answer += 1
        r += 1
        l += 1
print(answer)