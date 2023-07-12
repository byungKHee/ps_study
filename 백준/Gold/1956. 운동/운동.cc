#include <iostream>
using namespace std;
const int INF = 40000000;

int T, N, M;
int answer;
int cost[401][401];

void solve(){
    cin >> N >> M;
    for(int i = 1; i < N+1; i++){
        for(int j = 1; j < N+1; j++){
            cost[i][j] = INF;
        }
    }
    answer = INF;
    for(int i = 0; i < M; i++){
        int x, y, c; cin >> x >> y >> c;
        if(x == y){
            answer = c;
            continue;
        }
        cost[x][y] = min(cost[x][y], c);
    }
    for(int k = 1; k < N+1; k++){
        for(int i = 1; i < N+1; i++){
            if(cost[i][k] == INF) continue;
            for(int j = 1; j < N+1; j++){
                if(cost[i][j] > cost[i][k] + cost[k][j]){
                    cost[i][j] = cost[i][k] + cost[k][j];
                }
            }
        }
    }
    for(int node = 1; node < N+1; node++){
        answer = min(answer, cost[node][node]);
    }
    if(answer == INF){
        answer = -1;
    }
    cout << answer << '\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
    return 0;
}