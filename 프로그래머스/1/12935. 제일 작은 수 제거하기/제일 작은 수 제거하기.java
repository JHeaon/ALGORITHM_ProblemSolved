import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        if(arr.length == 1) return new int[]{-1};
        
        int min = arr[0];
        int[] answer = new int[arr.length - 1];
        
        for(int element: arr){
            if(min > element) min = element;
        }
        
        
        int index = 0;
        for(int element: arr){
            if(min != element){
                answer[index] = element;
                index++;
            }
        }        
        
        return answer;
  
    }
}