import java.util.*;

class Solution {

    
    public int solution(int[] stones, int k) {
        int answer = 200000001;
        Deque<Integer> q = new ArrayDeque<>(); // 단조 감소 큐
        for(int i = 0; i < k; i++){
            
            while (!q.isEmpty() && stones[q.peekLast()] < stones[i]){
                q.pollLast();   
            }
            q.offerLast(i);
        }
        answer = Math.min(answer, stones[q.peekFirst()]);
        
        for(int i = k; i < stones.length; i++){
            
            // 지나간 인덱스 정리
            if (q.peekFirst() + k <= i) q.pollFirst();
            
            // 모노톤 유지
            while (!q.isEmpty() && stones[q.peekLast()] < stones[i]) q.pollLast();
            q.offerLast(i);
            
            answer = Math.min(answer, stones[q.peekFirst()]);
            
        }
        
        
        return answer;
        
    }
}