import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        for(int i = 0; i < citations.length; i++) {
            if (i + 1 <= citations[citations.length - 1 - i]){
                answer = i + 1;
            }
            else{
                break;
            }
        }
        return answer;
    }
}