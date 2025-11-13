import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> s = new Stack<>();        
        for (var n : arr){
            if (s.empty() || s.peek() != n){
                s.push(n);
            }
        }
        
        return s.stream().mapToInt(n -> n).toArray();
    }
}