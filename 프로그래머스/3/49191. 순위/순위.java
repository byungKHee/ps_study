class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        boolean[][] possible = new boolean[n][n];
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                possible[i][j] = false;
            }
            possible[i][i] = true;
        }
        for (var a : results){
            possible[a[0]-1][a[1]-1] = true;
        }
        
        for (int k = 0; k < n; k++){
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    if (possible[i][j]) continue;
                    possible[i][j] = possible[i][k] && possible[k][j];
                }
            }
        }
        
        for(int curr = 0; curr < n; curr++){
            int count = 0;
            for (int next = 0; next < n; next++){
                if (curr == next) continue;
                if (possible[curr][next]) count++;
                if (possible[next][curr]) count++;
            }
            if (count == n-1) answer++;
        }
        
        return answer;
    }
}