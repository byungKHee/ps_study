import java.util.*;

class Solution {

    static int N;
    public String solution(int[] numbers) {
        N = numbers.length;
        String[] s = new String[N];
        for(int i = 0; i < N; i++){
            s[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(s, (a,b) -> (b+a).compareTo(a+b));
        StringBuilder sb = new StringBuilder();
        for (var a : s){
            sb.append(a);
        }
        var answer = sb.toString();
        if (answer.charAt(0) == '0'){
            return "0";
        }
        return answer;
    }
}