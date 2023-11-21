import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
answer = 0
for x in range(1, N+1):
    count = 0
    for nx in range(1, N+1):
        if nx == x: continue
        inter = False
        f = lambda a : (arr[x] - arr[nx]) * (a - x)/ (x - nx) + arr[x]
        for i in range(min(nx, x)+1, max(nx, x)):
            if f(i) <= arr[i]:
                inter = True
                break
        if not inter:
            count += 1
    answer = max(answer, count)
print(answer)