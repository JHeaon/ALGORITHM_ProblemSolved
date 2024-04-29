import java.util.*;

class Solution {
    public String solution(String s) {
        List<Character> string = new ArrayList<Character>();
        String answer = "";
        
        for(int i = 0; i < s.length(); i++){
            string.add(s.charAt(i));
        }
        
        Collections.sort(string, Collections.reverseOrder());
        
        for(Character element: string){
            answer += String.valueOf(element);
        }
        
        return answer;
    }
}