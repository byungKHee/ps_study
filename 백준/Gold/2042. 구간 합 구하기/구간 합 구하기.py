import sys
input = sys.stdin.readline

######################################
##### segment tree final version #####
######################################

def findSize():
    s = 0
    while 2**s < 2*N:
        s += 1
    return 2**s

def makeTree():
    tree = [0] * Size
    for i in range(N):
        tree[Size//2 + i] = data[i]
    for node in range(Size//2-1, 0, -1):
        tree[node] = tree[node*2] + tree[node*2+1]
    return tree

# [left, right) form
def subSum(node, nodeL, nodeR, targetL, targetR):
    if nodeR <= targetL or targetR <= nodeL:
        return 0
    if targetL <= nodeL and nodeR <= targetR:
        return segTree[node]
    mid = (nodeL + nodeR) // 2
    left = subSum(node*2, nodeL, mid, targetL, targetR)
    right = subSum(node*2+1, mid, nodeR, targetL, targetR)
    return left + right

# index start from 0
def update(i, num):
    node = Size//2 + i
    segTree[node] = num
    while node > 1:
        node = node // 2
        segTree[node] = segTree[node*2] + segTree[node*2+1]

# input data
N, M, K = map(int, input().split())
data = [int(input()) for _ in range(N)]

# build segment tree
Size = findSize()
segTree = makeTree()

# main process
for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b-1, c)
    else:
        print(subSum(1, 0, Size//2, b-1, c))