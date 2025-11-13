import java.util.*;


class Solution {

    static int curr = 0;
    static int answer = 0;

    public void bt(int idx, int[] numbers, int target){
        if (idx == numbers.length){
            if (target == curr) answer++;
            return;

        }
        // plus
        curr += numbers[idx];
        bt(idx+1, numbers, target);
        curr -= numbers[idx];
        
        // minus
        curr -= numbers[idx];
        bt(idx+1, numbers, target);
        curr += numbers[idx];
    }
    
    public int solution(int[] numbers, int target) {
        bt(0, numbers, target);
        return answer;
    }
}