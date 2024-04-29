class Solution {
    public boolean solution(String s) {
        
        if(s.length() == 4 || s.length() == 6){
            char[] charArray = s.toCharArray();
        
            for(int i = 0; i < charArray.length; i++){
                if(!Character.isDigit(charArray[i])){
                    return false;
                }
            }
        
            return true;
        }
        
        return false;
         
    }
}