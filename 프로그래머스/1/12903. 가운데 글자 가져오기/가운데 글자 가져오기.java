class Solution {
    public String solution(String s) {
        String answer = "";
        
        int index = 0;
        
        if(s.length() % 2 == 1){
            index = s.length() / 2;
            answer += s.charAt(index);
        }
        else{
            index = s.length() / 2;
            answer += s.charAt(index - 1) + "" + s.charAt(index); 
        }
        
        return answer;
    }
}