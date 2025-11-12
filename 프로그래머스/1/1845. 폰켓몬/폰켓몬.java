import java.util.*;
class Solution {
    public int solution(int[] nums) {
        Set<Integer> s = new HashSet<>();        
        for(var n : nums) s.add(n);
        return Math.min(s.size(), nums.length/2);
    }
}