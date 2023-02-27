import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
gold = []
bags = []
for _ in range(N):
    gold.append(list(map(int, input().split())))
for _ in range(K):
    bags.append(int(input()))
gold.sort()
bags.sort()
answer = 0
Q = []
for bag in bags:
    while gold and gold[0][0] <= bag:
        heapq.heappush(Q, -heapq.heappop(gold)[1])
    if Q:
        answer -= heapq.heappop(Q)
    elif not gold:
        break
print(answer)