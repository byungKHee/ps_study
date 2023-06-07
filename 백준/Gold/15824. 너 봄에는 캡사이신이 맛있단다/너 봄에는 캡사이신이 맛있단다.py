import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
DIVIDE = 1_000_000_007

def pow(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n % 2 == 0:
        half = pow(n//2)
        return half * half % DIVIDE
    else:
        half = pow(n//2)
        return half * half * 2 % DIVIDE

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
plus = 0
minus = 0
for i in range(N):
    if i == 0:
        minus += arr[i] * (pow(N-i-1) - 1) % DIVIDE
    elif i == N-1:
        plus += arr[i] * (pow(i) - 1) % DIVIDE
    else:
        plus += arr[i] * (pow(i) - 1) % DIVIDE
        minus += arr[i] * (pow(N-i-1) - 1) % DIVIDE
print((plus - minus) % DIVIDE)