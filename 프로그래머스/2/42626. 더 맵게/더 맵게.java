import java.util.*;

class Solution {
    
    public int solution(int[] scoville, int K) {
         int answer = 0;
        
        PriorityQueue<Long> Q = new PriorityQueue<>();
        for (int n : scoville) Q.offer((long)n);
        
        while (!Q.isEmpty()){
            if (Q.peek() >= K) break;
            if (Q.size() == 1){
                answer = -1;
                break;
            }
            else{
                var a = Q.poll();
                var b = Q.poll();
                Q.offer(a+b*2);
            }
            answer++;
        }
        
        return answer;
    }
}