import sys
input = sys.stdin.readline

def dfs(total, depth, plus, minus, multi, divide):
    if depth == N:
        answer[0] = max(answer[0], total)
        answer[1] = min(answer[1], total)
        return
    if plus:
        curr = total + A[depth]
        dfs(curr, depth+1, plus-1, minus, multi, divide)
    if minus:
        curr = total - A[depth]
        dfs(curr, depth+1, plus, minus-1, multi, divide)
    if multi:
        curr = total * A[depth]
        dfs(curr, depth+1, plus, minus, multi-1, divide)
    if divide:
        curr = total // A[depth]
        if total < 0:
            curr = (-1) * (((-1)*total) // A[depth])
        dfs(curr, depth+1, plus, minus, multi, divide-1)

N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))
answer = [float('-inf'), float('inf')]
dfs(A[0], 1, operator[0], operator[1], operator[2], operator[3])
for n in answer:
    print(n)