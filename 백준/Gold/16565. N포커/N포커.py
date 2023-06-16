import sys
input = sys.stdin.readline
DIVIDE = 10_007

def factorial(n):
    rnt = 1
    while n > 0:
        rnt *= n
        n -= 1
    return rnt

def comb(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

N = int(input())
if N < 4:
    print(0)
    sys.exit()
a = N // 4
b = N % 4

answer = 0
for i in range(1, a+1):
    answer += (-1)**(i+1) * comb(13, i) * comb(52-4*i, N-4*i)
    answer %= DIVIDE
print(answer)