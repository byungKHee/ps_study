import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def findSize():
    s = 0
    while 2**s <= 2*N:
        s += 1
    return 2**s

def makeTree(node, left, right):
    if left + 1 == right:
        segTree[node] = left
    else:
        mid = (left + right) // 2
        leftIdx = makeTree(node*2, left, mid)
        rightIdx = makeTree(node*2+1, mid, right)
        if arr[leftIdx] <= arr[rightIdx]:
            segTree[node] = leftIdx
        else:
            segTree[node] = rightIdx
    return segTree[node]

def getIdx(node, nodeL, nodeR, targetL, targetR):
    if targetR <= nodeL or nodeR <= targetL:
        return -1 # arr[-1] = INF
    if targetL <= nodeL and nodeR <= targetR:
        return segTree[node]
    mid = (nodeL + nodeR) // 2
    leftIdx = getIdx(node*2, nodeL, mid, targetL, targetR)
    rightIdx = getIdx(node*2+1, mid, nodeR, targetL, targetR)
    if arr[leftIdx] <= arr[rightIdx]:
        return leftIdx
    else:
        return rightIdx

def query(left, right):
    if left + 1 == right:
        return arr[left]
    if left >= right:
        return 0
    mid = getIdx(1, 0, N, left, right)
    midSquare = (right - left) * arr[mid]
    leftSqure = query(left, mid)
    rightSquare = query(mid+1, right)
    return max(leftSqure, midSquare, rightSquare)

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.append(float('inf'))
treeSize = findSize()
segTree = [-1] * treeSize
makeTree(1,0,N)
print(query(0,N))