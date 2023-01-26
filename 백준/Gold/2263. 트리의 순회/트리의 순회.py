import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def func(in_start, in_end, post_start, post_end):
    if (in_start >= in_end) or (post_start >= post_end):
        return

    parent = postorder[post_end-1]
    print(parent, end=' ')
    left_len = position[parent] - in_start
    right_len = in_end - position[parent] - 1

    func(in_start, position[parent], post_start, post_start+left_len)
    func(position[parent]+1, in_end, post_start+left_len, post_end-1)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0 for _ in range(N+1)]
for i in range(N):
    position[inorder[i]] = i
func(0, N, 0, N)