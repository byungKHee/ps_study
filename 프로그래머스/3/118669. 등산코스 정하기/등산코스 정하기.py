from heapq import heappush, heappop
IMPOSSIBLE = 100000000
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    
    answer = [n+1, IMPOSSIBLE]
    
    for a,b,w in paths:
        graph[a].append([b,w])
        graph[b].append([a,w])

    def func():
        nonlocal gates, summits, answer
        summit_check = set(summits)
        gates_check = set(gates)
        Q = []
        for start in gates:
            heappush(Q, [0, start])
        dis = [IMPOSSIBLE] * (n+1) # start -> node까지의 intensity 최솟값
        
        min_dis = IMPOSSIBLE
        min_end = n+1
        
        while Q:
            curr_dis, curr_node = heappop(Q)
            if curr_dis > dis[curr_node]: continue
            
            if curr_node in summit_check:
                if answer[1] > curr_dis:
                    answer = [curr_node, curr_dis]
                elif answer[1] == curr_dis and answer[0] > curr_node:
                    answer = [curr_node, curr_dis]
                continue
            
            for next_node, next_w in graph[curr_node]:
                if next_node in gates_check: continue
                new_dis = max(curr_dis, next_w)
                if dis[next_node] == IMPOSSIBLE or dis[next_node] > new_dis:
                    dis[next_node] = new_dis
                    heappush(Q, [new_dis, next_node])

    func()
    return answer