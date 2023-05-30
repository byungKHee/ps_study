import sys
input = sys.stdin.readline

def dfs(idx, A, B):
    global answer
    if idx == N:
        diff = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                diff += S[A[i]][A[j]]
        for i in range(len(B)-1):
            for j in range(i+1, len(B)):
                diff -= S[B[i]][B[j]]
        answer = min(answer, abs(diff))
        return
    if len(A) < (N//2):
        next = A[:]
        next.append(idx)
        dfs(idx+1, next, B[:])
    if len(B) < (N//2):
        next = B[:]
        next.append(idx)
        dfs(idx+1, A[:], next)

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        S[i][j] += S[j][i]
answer = float('inf')
dfs(0, [], [])
print(answer)