import sys
input = sys.stdin.readline

def findSize():
    size = 1
    while size < 2 * N:
        size *= 2
    return size

def makeTree(node, left, right):
    if left + 1 >= right:
        segTree[node] = left
        leafNode[left] = node
        return
    mid = (left + right) // 2
    makeTree(node*2, left, mid)
    makeTree(node*2+1, mid, right)
    if arr[segTree[node*2]] <= arr[segTree[node*2+1]]:
        segTree[node] = segTree[node*2]
    else:
        segTree[node] = segTree[node*2+1]

def query(node, nodeL, nodeR, targetL, targetR):
    if targetR <= nodeL or nodeR <= targetL:
        # arr[N] -> inf
        return N
    if targetL <= nodeL and nodeR <= targetR:
        return segTree[node]
    mid = (nodeL + nodeR) // 2
    leftIdx = query(node*2, nodeL, mid, targetL, targetR)
    rightIdx = query(node*2+1, mid, nodeR, targetL, targetR)
    if arr[leftIdx] <= arr[rightIdx]:
        return leftIdx
    else:
        return rightIdx

def update(idx, value):
    arr[idx] = value
    curr = leafNode[idx] // 2
    while curr > 0:
        if arr[segTree[curr*2]] <= arr[segTree[curr*2+1]]:
            segTree[curr] = segTree[curr*2]
        else:
            segTree[curr] = segTree[curr*2+1]
        curr //= 2

def printTree(depth):
    if 2**depth >= Size:
        return
    for i in range(2**depth, 2**(depth+1)):
        print(segTree[i], end= ' ')
    print()
    printTree(depth+1)

# input data
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# segment tree setting
Size = findSize()
arr.append(float('inf'))
segTree = [N] * Size
leafNode = [0] * N
makeTree(1, 0, N)

# input query
for _ in range(M):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b-1,c)
    else:
        print(query(1, 0, N, b-1, c)+1)