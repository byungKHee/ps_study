import java.util.*;

class Solution {
    
    static Map<String, Integer> cnt;
    static Map<String, List<String>> graph;
    
    static List<String> answer;
    static List<String> curr;
    static int total;
    
    boolean bt(String node, int used){
        boolean rnt = false;
        curr.add(node);
        if (used == total){
            answer = new ArrayList<>(curr);
            return true;
        }
        else{
            for (String next : graph.getOrDefault(node, new ArrayList<String>())){
                
                if (rnt == true) break;
                
                String move = node + " " + next;
                if (cnt.getOrDefault(move, 0) <= 0) continue;
                
                cnt.put(move, cnt.get(move) - 1);
                rnt = bt(next, used+1);
                cnt.put(move, cnt.get(move) + 1);
            }
        }        
        curr.remove(curr.size() - 1);
        return rnt;
    }
    
    
    public String[] solution(String[][] tickets) {
        
        cnt = new HashMap<>();
        graph = new HashMap<>();
        answer = new ArrayList<>();
        curr = new ArrayList<>();
        total = 0;
        
        for (var t : tickets){
            String s = t[0];
            String e = t[1];
            
            // 티켓 개수 설정
            String name = s + " " + e;
            cnt.put(name, cnt.getOrDefault(name, 0) + 1);
            total++;
            
            // graph 설정
            List<String> v = graph.getOrDefault(s, new ArrayList<String>());
            v.add(e);
            graph.put(s, v);
        }
        
        // 내부 노드 정렬
        List<String> startNode = new ArrayList<>();
        
        for(var p : graph.entrySet()){
            var v = p.getValue();
            Collections.sort(v);
        }
        bt("ICN",0);
        
        return answer.toArray(new String[0]);
    }
}