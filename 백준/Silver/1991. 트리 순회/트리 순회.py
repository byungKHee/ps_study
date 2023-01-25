import sys
input = sys.stdin.readline

def CtoD(c):
    if c == ".": return -1
    else: return ord(c)-65
def DtoC(d):
    return chr(d+65)

def preorder(start):
    if start == -1:
        return
    l, r = tree[start]
    print(DtoC(start), end='')
    preorder(l)
    preorder(r)
    
def inorder(start):
    if start == -1:
        return
    l, r = tree[start]
    inorder(l)
    print(DtoC(start), end='')
    inorder(r)
        
def postorder(start):
    if start == -1:
        return
    l, r = tree[start]
    postorder(l)
    postorder(r)
    print(DtoC(start), end='')

N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N):
    root, left, right = map(CtoD, input().rstrip().split())
    tree[root].append(left)
    tree[root].append(right)
preorder(0)
print()
inorder(0)
print()
postorder(0)