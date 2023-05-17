import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key, fullname):
        self.key = key
        self.children = {}
        self.fullname = fullname
        self.final = 0

class Trie:
    def __init__(self):
        self.root = Node(None, None)
    
    def make(self, data):
        check = False
        currNode = self.root
        for i in range(len(data)):
            if data[i] not in currNode.children:
                currNode.children[data[i]] = Node(data[i], data[:i+1])
                if not check:
                    print(data[:i+1])
                    check = True
            currNode = currNode.children[data[i]]
            if i == len(data)-1:
                currNode.final += 1
        if not check:
            if currNode.final == 1:
                print(currNode.fullname)
            else:
                print(currNode.fullname + str(currNode.final))

N = int(input())
names = [input().rstrip() for _ in range(N)]
T = Trie()
for name in names:
    T.make(name)