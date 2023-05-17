import sys
input = sys.stdin.readline

for testCase in range(int(input())):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(input().rstrip())
    arr.sort()
    answer = True
    for i in range(N-1):
        temp = False
        for j in range(min(len(arr[i]), len(arr[i+1]))):
            if arr[i][j] != arr[i+1][j]:
                temp = True                
        answer = temp
        if not answer:
            break
    if answer:
        print("YES")
    else:
        print("NO")