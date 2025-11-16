class Solution {
    boolean solution(String s) {
        int p = 0;
        int y = 0;
        
        for (int i = 0; i < s.length(); i++){
            char target = s.charAt(i);
            if (target == 'p' || target == 'P') p++;
            if (target == 'y' || target == 'Y') y++;
        }

        return p == y;
    }
}