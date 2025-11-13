import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Stack<Character> stack = new Stack<>();
        for(char c : s.toCharArray()){
            if (stack.empty() || c == '('){
                stack.push(c);
            }
            else{
                if (stack.peek() == '('){
                    stack.pop();
                }
                else{
                    answer = false;
                    break;
                }
            }
        }
        if (!stack.empty()) answer = false;
        return answer;
    }
}