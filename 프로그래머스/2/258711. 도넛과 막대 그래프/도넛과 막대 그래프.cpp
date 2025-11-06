#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int N;
vector<vector<int>> graph;
vector<bool> visited;
vector<bool> finished;

int dfs(int curr){
    visited[curr] = true;
    // outdegree == 2 -> 3번 타입
    if (graph[curr].size() == 2){
        return 3;
    }
    
    for (int next : graph[curr]){
        if (visited[next]){
            return 1;
        }
        int rnt = dfs(next);
        if (rnt != 2){
            return rnt;
        }
    }
    return 2;
}

vector<int> solution(vector<vector<int>> edges) {
    vector<int> answer(4,0);
    N = 0;
    for (auto a : edges){
        N = max(N, max(a[0], a[1]));
    }
    graph.resize(N+1);
    vector<int> indegree(N+1, 0);
    vector<int> outdegree(N+1, 0);
    visited.resize(N+1, false);
    finished.resize(N+1, false);
    for(auto edge : edges) {
        int s = edge[0], e = edge[1];
        graph[s].push_back(e);
        indegree[e] += 1;
        outdegree[s] += 1;
    }
    for (int node = 1; node <= N; node++){
        if (indegree[node] == 0 && outdegree[node] >= 2){
            answer[0] = node;
        }
    }
    
    for (int target : graph[answer[0]]) {
        // for (int i = 1; i <= N; i++){
        //     visited[i] = false;
        //     finished[i] = false;
        // }
        visited[answer[0]] = true;
        answer[dfs(target)]++;
    }
    
    return answer;
}