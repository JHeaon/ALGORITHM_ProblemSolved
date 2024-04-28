import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        
        ArrayList<Integer> numbersList = new ArrayList<Integer>();
        for(int i = 0; i < numbers.length; i++){
            numbersList.add(numbers[i]);
        }
        
        int sum = 0;
        
        for(int i = 0; i < 10; i++){
            if(!numbersList.contains(i)){
                sum += i;
            }
        }
        
        return sum;
    }
}