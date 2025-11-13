import java.util.*;
class Solution {
    
    static List<List<Integer>> graph;
    static int N;
    static boolean[] visited;
    
    void dfs(int curr){
        visited[curr] = true;
        for (var next : graph.get(curr)){
            if (visited[next]) continue;
            dfs(next);
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        graph = new ArrayList<>();
        N = n;
        visited = new boolean[N];
        for(int i = 0; i < N; i++){
            graph.add(new ArrayList<Integer>());
            visited[i] = false;
        }
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if (i == j) continue;
                if (computers[i][j] == 1){
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
        
        for (int node = 0; node < N; node++){
            if (visited[node]) continue;
            dfs(node);
            answer++;
        }
        return answer;
    }
}