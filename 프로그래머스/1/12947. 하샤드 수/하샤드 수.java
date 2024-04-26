import java.util.*;

class Solution {
    public boolean solution(int x) {
        
        String[] xCharArray = (Integer.toString(x)).split("");
        
        int sum = 0;
        
        for(int i = 0; i < xCharArray.length; i++){
            sum += Integer.valueOf(xCharArray[i]);
            System.out.println(sum);
        }
        if(x % sum == 0){
            return true;
        }
        
        return false;
    }
}