import java.util.*;
class Solution {
    
    // 커지는 최초의 idx [s,e)
    int upper(int[] arr, int s, int e, int target){
        int l = s-1;
        int r = e;
        while (l + 1 < r){
            int mid = (l + r) / 2;
            if (arr[mid] > target) r = mid;
            else l = mid;
        }
        return r;
    }
    
    // 같거나 커지는 최초의 idx [s,e)
    int lower(int[] arr, int s, int e, int target){
        int l = s-1;
        int r = e;
        while (l + 1 < r){
            int mid = (l + r) / 2;
            if (arr[mid] >= target) r = mid;
            else l = mid;
        }
        return r;
    }
    
    public int[] solution(int[] sequence, int k) {
        int[] answer = {0,0};
        int N = sequence.length;
        int[] dp = new int[N+1];
        
        // 누적합
        dp[0] = 0;
        for (int i = 1; i < N+1; i++){
            dp[i] = dp[i-1] + sequence[i-1];
        }
    
        int min_length = N+2;
        for(int i = 0; i < N; i++){
            int target = dp[i] + k;
            
            int idx = lower(dp, i+1, N+1, target);
            if (idx == N+1) continue;
            if (dp[idx] - dp[i] == k){
                if (min_length > idx - i){
                    answer[0] = i;
                    answer[1] = idx-1;
                    min_length = idx - i;
                }
            }
            
        }
        
        
        return answer;   
    }
}