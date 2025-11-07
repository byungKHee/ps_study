#include<vector>
#include<queue>
using namespace std;

int N, M;
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

struct Node{
    int x;
    int y;
    int dis;
};

int solution(vector<vector<int> > maps)
{
    int answer = -1;
    N = maps.size();
    M = maps[0].size();
    
    bool visited[N][M];
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            visited[i][j] = false;
        }
    }
    
    queue<Node> Q;
    Q.push({0,0,1});
    visited[0][0] = true;
    
    while(!Q.empty()){
        auto [cx, cy, dis] = Q.front(); Q.pop();
        
        if (cx == N-1 && cy == M-1){
            answer = dis;
            break;
        }
        
        for (int i = 0; i < 4; i++){
            int nx = cx + dx[i], ny = cy + dy[i];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (visited[nx][ny] || maps[nx][ny] == 0) continue;
            
            Q.push({nx,ny,dis+1});
            visited[nx][ny] = true;
        }
        
    }
    
    return answer;
}