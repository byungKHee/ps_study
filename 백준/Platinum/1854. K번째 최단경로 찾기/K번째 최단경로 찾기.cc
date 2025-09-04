#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M, K;
vector<pair<int, int>> g[1000];
priority_queue<int> dis[1000];
int visit[1000];

void func(){
    priority_queue<pair<int, int>> Q;
    Q.push({0,0});
    dis[0].push(0);
    visit[0]++;
    while(!Q.empty()){
        auto curr = Q.top(); Q.pop();
        int curr_node = curr.second, curr_dis = -1 * curr.first;
        if(visit[curr_node] > K) continue;
        visit[curr_node]++;
        for(auto next : g[curr_node]){
            int next_node = next.first, w = next.second;
            int next_dis = curr_dis + w;
            if(dis[next_node].size() < K){
                dis[next_node].push(next_dis);
                Q.push({-1 * next_dis, next_node});

            }
            else{
                if(dis[next_node].top() > next_dis){
                    dis[next_node].pop();
                    dis[next_node].push(next_dis);
                    Q.push({-1 * next_dis, next_node});

                }
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    cin >> N >> M >> K;
    for(int i = 0; i < N; i++) visit[i] = 0;
    for(int i = 0; i < M; i++){
        int a,b,c; cin >> a >> b >> c;
        a--; b--;
        g[a].push_back({b,c});
    }
    func();
    for(int i = 0; i < N; i++){
        if(dis[i].size() < K){
            cout << "-1\n";
        }
        else{
            cout << dis[i].top() << '\n';
        }
    }
}