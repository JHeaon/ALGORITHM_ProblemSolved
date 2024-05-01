import java.util.*;

class Solution {
    public int solution(String t, String p) {
        ArrayList<String> answerList = new ArrayList<>();
        int answer = 0;
        
        for(int i = 0; i <= t.length() - p.length(); i++){
            answerList.add(t.substring(i, i + p.length()));
        }
        
        
        for(String value : answerList){
            if(Long.valueOf(value) <= Long.valueOf(p)){
                answer++;
            }
        }
        
        return answer;
    }
}