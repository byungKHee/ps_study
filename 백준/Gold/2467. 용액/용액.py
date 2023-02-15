import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
if arr[0] > 0:
    print(arr[0], arr[1])
elif arr[-1] < 0:
    print(arr[-2], arr[-1])
else:
    num = []
    for n in arr:
        if n > 0:
            num.append((n, 1))
        else:
            num.append((-n, -1))
    num.sort()
    total = num[-1][0] * 2
    x,y = 0,0
    for i in range(N-1):
        a,b = num[i]
        c,d = num[i+1]
        if abs(a*b+c*d) < total:
            total = abs(a*b+c*d)
            if a*b < c*d:
                x,y = a*b, c*d
            else:
                x,y = c*d, a*b
    print(x,y)