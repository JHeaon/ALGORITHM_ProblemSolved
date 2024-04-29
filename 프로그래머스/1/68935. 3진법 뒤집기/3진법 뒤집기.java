import java.util.*;

class Solution {
    public int solution(int n) {
        ArrayList<Integer> answer = new ArrayList<Integer>();

        while(true){
            answer.add(n % 3);
            if(n / 3 == 0) break;
            n /= 3;
        }
        
        double result = 0;
        int index = 0;
        
        for(int i = answer.size() - 1; i >= 0; i--){
            result += Math.pow(3, index++) * answer.get(i);
        }
        
        return (int)result;
    }
}