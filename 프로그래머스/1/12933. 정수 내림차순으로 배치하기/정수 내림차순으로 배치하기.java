import java.util.*;

class Solution {
    public long solution(long n) {
       
       String answer = "";
       String[] numberString = String.valueOf(n).split("");
       Arrays.sort(numberString, Collections.reverseOrder());
       
       for(String element : numberString){
           answer += element;
       }
        
       return Long.valueOf(answer);
        
    }
}