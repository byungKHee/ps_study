import sys
input = sys.stdin.readline

class Node:
    def __init__(self,key):
        self.key = key
        self.children = {}

class Tree:
    def __init__(self):
        self.root = Node(None)
    
    def printNode(self, depth, curr):
        print('--' * depth, end = '')
        print(curr.key)
        if curr.children:
            for idx in sorted(curr.children.keys()):
                self.printNode(depth+1, curr.children[idx])      

    def printTree(self):
        for idx in sorted(self.root.children.keys()):
            self.printNode(0, self.root.children[idx])

    def make(self, data):
        currNode = self.root
        for key in data:
            if key not in currNode.children:
                currNode.children[key] = Node(key)
            currNode = currNode.children[key]
        
N = int(input())
arr = []
for _ in range(N):
    arr.append(input().rstrip().split()[1:])
T = Tree()
for data in arr:
    T.make(data)
T.printTree()