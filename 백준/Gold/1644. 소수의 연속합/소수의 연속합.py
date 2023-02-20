import sys
input = sys.stdin.readline

def func():
    for i in range(2, N+1):
        if isPrime[i]:
            primeSum.append(i)
            for j in range(i*2, N+1, i):
                isPrime[j] = False
    for i in range(1, len(primeSum)):
        primeSum[i] += primeSum[i-1]

N = int(input())
isPrime = [True] * (N+1)
primeSum = [0]
func()
answer = 0
start,end = (0,0)
while True:
    if end == len(primeSum):
        break
    diff = primeSum[end] - primeSum[start]
    if diff == N:
        answer += 1
        start += 1
        end += 1
    elif diff < N:
        end += 1
    elif diff > N:
        start += 1
print(answer)