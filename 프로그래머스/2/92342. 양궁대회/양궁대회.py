def solution(n, info):
    arr = [(n+1, 10-i) for i, n in enumerate(info)]
    answer = []
    curr = []
    Total = 0
    def change(a):
        for i in range(10, 0, -1):
            if answer[i] < a[i]:
                return True
            if answer[i] > a[i]:
                return False
        return False
        
    def dfs(idx, left, total):
        nonlocal answer, curr, Total
        # 종료조건
        if idx == 11:
            if left > 0:
                curr[10] += left
            if Total == total and Total != 0:
                if change(curr):
                    answer = curr.copy()
            elif Total < total:
                answer = curr.copy()
                Total = total
            return
        
        if left >= arr[idx][0]:
            curr.append(arr[idx][0])
            dfs(idx+1, left - arr[idx][0], total + 10 - idx)
            curr.pop()
        curr.append(0)
        if info[idx] > 0:
            dfs(idx+1, left, total + idx - 10)
        else:
            dfs(idx+1, left, total)
        curr.pop()
    dfs(0,n,0)
    if Total == 0:
        return [-1]
    if not answer:
        return [-1]
    return answer