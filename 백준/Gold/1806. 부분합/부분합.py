import sys
input = sys.stdin.readline

N, Target = map(int, input().split())
num = list(map(int, input().split()))
num.insert(0,0)

start = 0
end = 0
answer = N+1
Sum = 0
while True:
    if Sum >= Target:
        if end - start + 1 < answer:
            answer = end - start + 1
        Sum -= num[start]
        start += 1
    if Sum < Target:
        if end == N:
            break
        end += 1
        Sum += num[end]
if answer == N+1:
    print(0)
else:
    print(answer)