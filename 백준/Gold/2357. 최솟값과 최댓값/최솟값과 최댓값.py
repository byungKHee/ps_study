import sys
input = sys.stdin.readline

def findSize():
    s = 0
    while 2**s < 2*N:
        s += 1
    return 2**s

def makeTree(t):
    if t == 0:
        tree = [float('inf')] * Size
        for i in range(N):
            tree[Size//2 + i] = data[i]
        for node in range(Size//2-1, 0, -1):
            tree[node] = min(tree[node*2], tree[node*2+1])
        return tree
    else:
        tree = [0] * Size
        for i in range(N):
            tree[Size//2 + i] = data[i]
        for node in range(Size//2-1, 0, -1):
            tree[node] = max(tree[node*2], tree[node*2+1])
        return tree

# [left, right) form
def find(node, nodeL, nodeR, targetL, targetR):
    if nodeR <= targetL or targetR <= nodeL:
        return [float('inf'), 0]
    if targetL <= nodeL and nodeR <= targetR:
        return [minTree[node], maxTree[node]]
    mid = (nodeL + nodeR) // 2
    left = find(node*2, nodeL, mid, targetL, targetR)
    right = find(node*2+1, mid, nodeR, targetL, targetR)
    return [min(left[0], right[0]), max(left[1], right[1])]

N, M = map(int, input().split())
data = [int(input()) for _ in range(N)]

Size = findSize()
minTree = makeTree(0)
maxTree = makeTree(1)

for _ in range(M):
    a,b = map(int, input().split())
    print(*find(1, 0, Size//2, a-1, b))