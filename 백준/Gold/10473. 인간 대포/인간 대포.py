import sys
import heapq
input = sys.stdin.readline

def dis(start, end):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    return (dx**2 + dy**2) ** 0.5

def func(start, end):
    Dis[start] = 0
    Q = []
    for i in range(1, len(Node)):
        Dis[i] = dis(Node[0], Node[i]) / 5
        heapq.heappush(Q, (Dis[i], i))
    while Q:
        curr_dis, curr_node = heapq.heappop(Q)
        if curr_node == N+1:
            continue
        if curr_dis > Dis[curr_node]:
            continue
        for i in range(1, len(Node)):
            if i == curr_node:
                continue
            distance = dis(Node[curr_node], Node[i])
            walk = distance / 5
            fly = 2 + (abs(distance-50)/5)
            next_w = min(walk, fly)
            if curr_dis + next_w < Dis[i]:
                Dis[i] = curr_dis + next_w
                heapq.heappush(Q, (Dis[i], i))
    return Dis[end]

Node = []
start = tuple(map(float, input().split()))
end = tuple(map(float, input().split()))
N = int(input())
Node.append(start)
for _ in range(N):
    Node.append(tuple(map(float, input().split())))
Node.append(end)
Dis = [float("inf") for _ in range(N+2)]

print(func(0, N+1))