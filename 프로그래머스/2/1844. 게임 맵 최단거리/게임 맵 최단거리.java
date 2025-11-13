import java.util.*;

class Solution {
    
    class Node{
        int x;
        int y;
        int dis;
        Node(int x, int y, int dis){
            this.x = x;
            this.y = y;
            this.dis = dis;
        }
    }
    
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    
    public int solution(int[][] maps) {
        int answer = -1;
        int N = maps.length;
        int M = maps[0].length;
        Queue<Node> Q = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][M];
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++){
                visited[i][j] = false;
            }
        }
        
        Q.offer(new Node(0,0,1));
        visited[0][0] = true;
        
        while(!Q.isEmpty()){
            var curr = Q.poll();
            int cx = curr.x, cy = curr.y, dis = curr.dis;
            
            if (cx == N-1 && cy == M-1){
                answer = dis;
                break;
            }
            
            for(int i = 0; i < 4; i++){
                int nx = cx + dx[i], ny = cy + dy[i];
                if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
                if (visited[nx][ny] || maps[nx][ny] == 0) continue;
                Q.offer(new Node(nx,ny,dis+1));
                visited[nx][ny] = true;
            }
        }
        
        return answer;
    }
}