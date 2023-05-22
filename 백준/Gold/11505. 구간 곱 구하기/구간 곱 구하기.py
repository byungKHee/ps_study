import sys
input = sys.stdin.readline

DIVIDE = 1000000007

def findSize():
    s = 0
    while 2**s < 2*N:
        s += 1
    return 2**s

def makeTree():
    tree = [1] * Size
    for i in range(N):
        tree[Size//2 + i] = data[i]
    for i in range(Size//2-1, 0, -1):
        tree[i] = tree[i*2] * tree[i*2+1] % DIVIDE
    return tree
    
# [left, right) form
def func(node, nodeL, nodeR, targetL, targetR):
    if nodeR <= targetL or targetR <= nodeL:
        return 1
    if targetL <= nodeL and nodeR <= targetR:
        return segTree[node]
    mid = (nodeL + nodeR) // 2
    left = func(node*2, nodeL, mid, targetL, targetR)
    right = func(node*2+1, mid, nodeR, targetL, targetR)
    return left * right % DIVIDE

def update(i, num):
    node = Size//2 + i
    segTree[node] = num
    while node > 1:
        node = node // 2
        segTree[node] = segTree[node*2] * segTree[node*2+1] % DIVIDE

N, M, K = map(int, input().split())
data = [int(input()) for _ in range(N)]

Size = findSize()
segTree = makeTree()

for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b-1, c)
    else:
        print(func(1, 0, Size//2, b-1, c))