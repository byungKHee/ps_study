import sys
input = sys.stdin.readline

def func(target, idx):
    if idx == 0:
        target[idx] = not target[idx]
        target[idx+1] = not target[idx+1]
    elif idx == N-1:
        target[idx-1] = not target[idx-1]
        target[idx] = not target[idx]
    else:
        for i in range(idx-1, idx+2):
            target[i] = not target[i]

N = int(input())
arr = list(map(lambda x : bool(int(x)), list(input().rstrip())))
target = list(map(lambda x : bool(int(x)), list(input().rstrip())))

arr1 = arr[:]
arr2 = arr[:]
count1 = 1
count2 = 0
func(arr1, 0)
for i in range(N-1):
    if arr1[i] != target[i]:
        func(arr1, i+1)
        count1 += 1
    if arr2[i] != target[i]:
        func(arr2, i+1)
        count2 += 1
answer = 1000000
if arr1[-1] == target[-1]:
    answer = count1
if arr2[-1] == target[-1]:
    answer = min(answer, count2)
if answer == 1000000:
    print(-1)
else:
    print(answer)