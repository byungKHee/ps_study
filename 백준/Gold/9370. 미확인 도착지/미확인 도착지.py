import sys
from heapq import heappop, heappush
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def func():
    dis[S] = 0
    Q = [[0, S]]
    while Q:
        curr_dis, curr_node = heappop(Q)
        if curr_dis > dis[curr_node]:
            continue
        for next_node, next_w in graph[curr_node]:
            if curr_dis + next_w < dis[next_node]:
                dis[next_node] = curr_dis + next_w
                prev[next_node].clear()
                prev[next_node].add(curr_node)
                heappush(Q, [dis[next_node], next_node])
            if curr_dis + next_w == dis[next_node]:
                prev[next_node].add(curr_node)

def dfs(curr_node):
    flag = False
    for prev_node in prev[curr_node]:
        if curr_node == G and prev_node == H:
            flag = True
        if curr_node == H and prev_node == G:
            flag = True
        if flag:
            break
        else:
            flag = dfs(prev_node)
    return flag
    
def possible_route(node):
    if dis[node] == float('inf'):
        return False
    if dfs(node):
        return True
    else:
        return False

for testCase in range(int(input())):
    V, E, T = map(int, input().split())
    S, G, H = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    target = []
    for _ in range(E):
        a,b,d = map(int, input().split())
        graph[a].append([b,d])
        graph[b].append([a,d])
    for _ in range(T):
        target.append(int(input()))
    dis = [float('inf') for _ in range(V+1)]
    prev = [set() for _ in range(V+1)]
    func()
    for node in sorted(target):
        if possible_route(node):
            print(node, end=' ')
    print()