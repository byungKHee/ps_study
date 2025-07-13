#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int N = 0;
vector<vector<int>> graph;
vector<int> indegree;
vector<bool> visited;

int start_node;

// 0: 막대, 1: 도넛, 2: 결합
int findType(int curr){
    visited[curr] = true;
    int rnt = 0;
    if (graph[curr].size() >= 2){
        return 2;
    }
    for(int& next : graph[curr]){
        if(visited[next]){
            rnt = 1;
            break;
        }
        rnt = findType(next);
        if(!rnt){
            break;
        }
    }
    return rnt;
}

vector<int> solution(vector<vector<int>> edges) {
    vector<int> answer(4, 0);

    for(const auto& node : edges){
        N = max({N, node[0], node[1]});
    }
    graph.resize(N+1);
    indegree.resize(N+1, 0);
    visited.resize(N+1, false);
    for(const auto& node : edges){
        graph[node[0]].push_back(node[1]);
        indegree[node[1]]++;
    }
    // 시작 노드 찾기
    int M = 0;
    for(int i = 1; i < N+1; i++){
        if(indegree[i]) continue;
        if(M < graph[i].size()){
            start_node = i;
            M = graph[i].size();
        }
    }
    cout << start_node << endl;
    answer[0] = start_node;
    
    for(int& next : graph[start_node]){
        int rnt = findType(next);
        if(rnt == 0){
            answer[2]++;
        }
        else if(rnt == 1){
            answer[1]++;
        }
        else{
            answer[3]++;
        }
    }
    return answer;
}