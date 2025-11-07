#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

struct music{
    int plays;
    int id;
    
    bool operator<(const music& other) {
        if (plays != other.plays) return plays > other.plays;
        return id < other.id;
    }
};

unordered_map<string, int> cnt;
unordered_map<string, vector<music>> dict;
int N;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    N = genres.size();
    for (int i = 0; i < N; i++){
        if (cnt.count(genres[i]) == 0) cnt[genres[i]] = 0;
        cnt[genres[i]] += plays[i];
        dict[genres[i]].push_back({plays[i], i});
    }
    
    vector<pair<int, string>> order;
    // 1. genre 순서
    for (auto& p : cnt){
        order.push_back({p.second, p.first});
    }
    sort(order.begin(), order.end());
    
    // 역순으로 먼저 탐색
    for (auto i = order.rbegin(); i != order.rend(); i++){
        string genre = i->second;
        
        sort(dict[genre].begin(), dict[genre].end());
        for (int i = 0; i < min(2, (int)dict[genre].size()); i++){
            answer.push_back(dict[genre][i].id);
        }   
    }
    
    return answer;
}