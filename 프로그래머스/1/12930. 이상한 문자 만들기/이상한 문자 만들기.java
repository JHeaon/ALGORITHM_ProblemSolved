class Solution {
    public String solution(String s) {
        String[] stringCase = s.split(" ", -1);
        String answer = "";
        
        for(int i = 0; i < stringCase.length; i++){
            String word = "";
            
            for(int j = 0; j < stringCase[i].length(); j++){
                if(j % 2 == 0){
                    word += Character.toUpperCase(stringCase[i].charAt(j));
                }
                else{
                    word += Character.toLowerCase(stringCase[i].charAt(j));
                }
            }
            
            answer += word;
            
            if(i != stringCase.length - 1){
                answer += " ";
            }
        }
        
        return answer;
    }
}