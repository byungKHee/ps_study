#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

#define IMPOSSIBLE 3000

int arr[50][50],visited[50][50], N, M, answer = IMPOSSIBLE;
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

vector<int> virus;
vector<int> selected;

struct elem{
    int x;
    int y;
    int dis;
};

void bfs(){
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            visited[i][j] = 0;
        }
    }
    deque<elem> Q;
    for(int v : selected){
        Q.push_back({v/N, v%N, 1});
        visited[v/N][v%N] = 1;
    }
    
    while(!Q.empty()){
        auto curr = Q.front();
        Q.pop_front();
        for(int i = 0; i < 4; i++){
            int nx = curr.x + dx[i];
            int ny = curr.y + dy[i];
            if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
            if(visited[nx][ny] || arr[nx][ny] == 1) continue;
            
            Q.push_back({nx,ny,curr.dis+1});
            visited[nx][ny] = curr.dis+1;
        }
    }
    bool possible = true;
    for (int v : virus){
        visited[v/N][v%N] = 1;
    }
    int rnt = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(arr[i][j] == 1) continue;
            if(!visited[i][j]){
                possible = false;
                break;
            }
            rnt = max(rnt, visited[i][j]);
        }
    }
    rnt--;
    if(possible){
        answer = min(answer, rnt);
    }
}

void bt(int curr){
    selected.push_back(virus[curr]);
    if(selected.size() == M){
        bfs();
    }
    else{
        for(int next = curr+1; next < virus.size(); next++){
            bt(next);
        }
    }
    selected.pop_back();
}


int main(){
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> N >> M;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> arr[i][j];
            if(arr[i][j] == 2){
                virus.push_back(i*N + j);
            }
        }
    }
    for(int idx = 0; idx < virus.size() - M + 1; idx++){
        bt(idx);
    }
    
    if(answer == IMPOSSIBLE) cout << "-1\n";
    else cout << answer << '\n';
}