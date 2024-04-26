import java.util.*;

class Solution {
    public long[] solution(long n) {
        
        String[] nString = Long.toString(n).split("");
        long[] answer = new long[nString.length];
        int count = 0;
            
        for(int i = nString.length - 1; i >= 0; i--){
            answer[count] = Long.valueOf(nString[i]);
            count++;
        }
        
        return answer;
               
    }
}