import java.util.*;

class Solution {
    public Integer[] solution(int[] arr, int divisor) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int value : arr){
            if(value % divisor == 0){
                answer.add(value);
            }
        }
        
        Collections.sort(answer);
        Integer[] answerArray = answer.toArray(new Integer[answer.size()]);
        
        if (answerArray.length == 0){
            return new Integer[]{-1};
        }
              
        return answerArray;
    }
}