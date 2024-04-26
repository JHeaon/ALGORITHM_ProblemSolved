public class Solution {
    public int solution(int n) {
        int answer = 0;
        int temp;
               
        while(true){
            
            temp = n % 10;
            answer += temp;
            n /= 10;
            
            if(n < 1){
                break;
            }
            
        }
        
        return answer;
    }
}