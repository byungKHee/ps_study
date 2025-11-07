#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

struct Task {
    int cost;
    int call;
    int id;
    
    bool operator<(const Task& other) const {
        if (cost == other.cost){
            if (call == other.call){
                return id > other.id;
            }
            return call > other.call;
        }
        return cost > other.cost;
    }   
};

int solution(vector<vector<int>> jobs) {
    int total = 0;
    int cnt = 0;
    sort(jobs.begin(), jobs.end(), [](const auto& a, const auto &b){
        return a[0] < b[0];
    });
    deque<vector<int>> job(jobs.begin(), jobs.end());
    priority_queue<Task> wait;
    
    int left = jobs.size();
    int id = 0;
    while(left){
        // 현재 시각 기준으로 job에서 요청이 들어온거 wait로 집어넣기
        while (!job.empty() && job.front()[0] <= cnt){
            auto j = job.front(); job.pop_front();
            wait.push({j[1], j[0], id});
            id += 1;
        }
        
        if (wait.empty()){
            cnt = job.front()[0];
        }
        else{
            // 가장 우선순위가 높은거 꺼내서 작업하기
            auto curr = wait.top(); wait.pop();
            cnt += curr.cost;
            total += cnt - curr.call;
            left -= 1;
        }
    }
    
    return total / jobs.size();
}