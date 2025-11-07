#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

unordered_map<string, vector<string>> graph;
unordered_map<string, int> visited;
int total;
bool finish = false;
vector<string> answer;

void bt(string curr){
    
    answer.push_back(curr);
    
    if (answer.size() == total + 1){
        finish = true;
        return;
    }
    
    for(string& next : graph[curr]){
        string path = curr + next;
        if (visited[path] <= 0) continue;
        visited[path] -= 1;
        bt(next);
        if (finish) return;
        visited[path] += 1;
    }
    answer.pop_back();
    
}


vector<string> solution(vector<vector<string>> tickets) {
    total = tickets.size();
    
    for(auto& ticket : tickets){
        graph[ticket[0]].push_back(ticket[1]);
        string path = ticket[0] + ticket[1];
        if (!visited.count(path)) visited[path] = 0;
        visited[path] += 1;
    }
    for (auto& nodes : graph){
        sort(nodes.second.begin(), nodes.second.end());
    }
    
    // // 0. 출발점 정하기 -> 사전순으로 빠른 곳부터 출발
    // vector<string> order;
    // for (auto& p : graph){
    //     order.push_back(p.first);
    // }
    // sort(order.begin(), order.end());

    bt("ICN");
    return answer;
}