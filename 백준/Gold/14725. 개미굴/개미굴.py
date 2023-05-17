import sys
input = sys.stdin.readline

Tree = {}

def make(curr, data):
    if not data:
        return
    if data[0] not in curr:
        curr[data[0]] = {}
    make(curr[data[0]], data[1:])
    
def printTree(curr, depth):
    for key in sorted(curr.keys()):
        print('--' * depth, end = '')
        print(key)
        printTree(curr[key], depth+1)

N = int(input())
arr = []
for _ in range(N):
    arr.append(input().rstrip().split()[1:])
for data in arr:
    make(Tree, data)
printTree(Tree, 0)