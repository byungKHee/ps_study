import sys
import math
input = sys.stdin.readline

def make(node, start, end):
    if start + 1 == end:
        tree[node] = num[start]
        leafIdx[start] = node
        return tree[node]
    else:
        mid = (start + end) // 2
        left = make(node*2, start, mid)
        right = make(node*2+1, mid, end)
        tree[node] = left + right
        return tree[node]

def subSum(node, nodeL, nodeR, targetL, targetR):
    if nodeR <= targetL or targetR <= nodeL:
        return 0
    if targetL <= nodeL and nodeR <= targetR:
        return tree[node]
    mid = (nodeL + nodeR) // 2
    left = subSum(node*2, nodeL, mid, targetL, targetR)
    right = subSum(node*2+1, mid, nodeR, targetL, targetR)
    return left + right

def update(idx, val):
    node = leafIdx[idx]
    tree[node] = val
    while node > 1:
        node //= 2
        tree[node] = tree[node*2] + tree[node*2+1]

N, M, K = map(int, input().split())
num = []
tree = [0] * 3000000
leafIdx = [0] * N
for _ in range(N):
    num.append(int(input()))
make(1, 0, N)
for i in range(M+K):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b-1, c)
    else:
        print(subSum(1, 0, N, b-1, c))