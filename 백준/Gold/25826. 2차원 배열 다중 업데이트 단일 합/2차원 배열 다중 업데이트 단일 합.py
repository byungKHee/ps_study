import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

imos = [[0] * (len(A[0]) + 1) for _ in range(len(A) + 1)]

for _ in range(M-1):
    _, r1, c1, r2, c2, value = map(int, input().split())
    imos[r1][c1] += value
    imos[r1][c2+1] -= value
    imos[r2+1][c1] -= value
    imos[r2+1][c2+1] += value

for i in range(len(A) + 1):
    for j in range(len(A[0])):
        imos[i][j+1] += imos[i][j]

for j in range(len(A[0]) + 1):
    for i in range(len(A)):
        imos[i+1][j] += imos[i][j]

_, x1, y1, x2, y2 = map(int, input().split())
answer = 0
for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        answer += imos[i][j] + A[i][j]
        
print(answer)