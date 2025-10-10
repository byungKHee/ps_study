from copy import deepcopy

answer = -1
arr = []
def dfs(cnt, curr, visited):
    global arr, answer
    answer = max(answer, cnt)
    for i in range(len(arr)):
        if i in visited: continue
        if arr[i][0] <= curr:
            next = deepcopy(visited)
            next.add(i)
            dfs(cnt + 1, curr - arr[i][1], next)

def solution(k, dungeons):
    global arr
    arr = dungeons
    dfs(0, k, set())
    
    return answer