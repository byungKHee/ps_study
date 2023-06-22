import sys
from itertools import combinations
input = sys.stdin.readline
MAX = 10**6

N = int(input())
isPrime = [True] * (MAX+1)
factors = []
for i in range(2, MAX+1):
    if i > N:
        break
    if isPrime[i]:
        if N % i == 0:
            factors.append(i)
        for j in range(i*i, MAX+1, i):
            isPrime[j] = False
temp = N
for n in factors:
    while temp % n == 0:
        temp //= n
if temp != 1:
    factors.append(temp)
answer = 0
for i in range(1, len(factors) + 1):
    for comb in combinations(factors, i):
        curr = 1
        for n in comb:
            curr *= n
        answer += ((-1)**(i+1)) * (N // curr)
print(N - answer)