import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> m = new HashMap<>();
        for (var name : completion){
            m.put(name, m.getOrDefault(name, 0) + 1);
        }
        String answer = new String();
        for (var name : participant){
            if(!m.containsKey(name) || m.get(name) == 0){
                answer = name;
                break;
            }
            m.put(name, m.get(name) - 1);
        }
        return answer;
    }
}